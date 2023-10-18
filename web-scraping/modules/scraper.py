# -- Import required libraries / modules:
from bs4 import BeautifulSoup as bs
from importlib import util
from requests import get
from pathlib import Path
from sys import modules

from modules.replace import replace_chars
from modules.config import OUTPUT_DIR

import inspect
import logging
import os
import pandas as pd


def url_scraper(url: str,
                allowed_http_responses: pd.DataFrame, 
                headers: dict,
                nickname: str, 
                site_name: str,
                parser: str = "html.parser"):
    """
    ### Summary:
        This function will scrape a web page and process it using
        BeautifulSoup.
    
    ### Args:
        url (str): 
            The URL that needs to be scraped.
        allowed_http_responses (dataframe): 
            A dataframe with a list of HTTP responses.
        headers (dict): 
            A dictionary containing the required headers.
        nickname (str):
            The nickname of the page to process.
        site_name (str):
            The name of the site folder that is used.
        parser (str, optional): 
            The parser that is used to render the web page. 
            Options are 'html.parser' or 'xml.parser'.
            Defaults to "html.parser".
        
    ### Returns:
        Object: The processed web page as a BeautifulSoup object.
    """
    
    # -- Initialise logging:
    log = logging.getLogger(f"{os.getenv('SCRAPER_APP_NAME')}.{__name__}.{inspect.stack()[0][3]}.{site_name}.{nickname}")
    #log = logging.getLogger(f"{os.getenv('SCRAPER_APP_NAME')}.{__name__}.{inspect.stack()[0][3]}.{nickname}")
    
    # -- Make a request to the site:
    log.info(f"Performing request.get for {nickname}.")
    log.info(f"URL for {nickname} is: {url}.")
    
    request = get(url = url, headers = headers)
    
    # -- Check the status code or the response is ok:
    log.info("Checking if the response code from the request is in the allowed list.")
    if request.status_code in allowed_http_responses:
        log.info(f"The response code for {nickname} is ok.")
        # -- Process and return the response with bs: 
        return bs(request.text, parser)
    else:
        print(f"Error: The response code {request.status_code} is not in the allowed list. Unable to continue processing {nickname}.")
        log.error((f"Error: The response code {request.status_code} is not in the allowed list. Unable to continue processing {nickname}."))
        return
        

def processor(allowed_http_responses: pd.DataFrame,
              browser_headers_os: pd.DataFrame,
              site_folder: str):
    """
    ### Summary:
        This function will:
        - process the files that are in the site_folder.
        - create a folder for the site in the output folder.
        - Cycle through each row in the pages.xlsx file and pass the output 
          over to the url_scraper function.
        - Finally, it will then pass the scraped page (as a beautiful soup object)
          to the process_soup function in the processor file.

    ### Args:
        allowed_http_responses (pd.DataFrame): 
            A dataframe containing the HTTP responses that are used to allow 
            the processing to continue.
        browser_headers_os (pd.DataFrame): 
            A filtered dataframe of browsers and
            headings for the operating system the program is running on.
        site_folder (str): 
            The full path for the site folder that is being processed.
    
    ### Returns:
        None
    """
    
    # -- Get the site name from the site_folder:
    site_name = str(site_folder).rsplit('/', 1)
    site_name = site_name[1]
    site_name = replace_chars(text_to_check = site_name)
    
    # -- Initialise logging:
    log = logging.getLogger(f"{os.getenv('SCRAPER_APP_NAME')}.{__name__}.{inspect.stack()[0][3]}.{site_name}")
    
    # -- Load the contents of the pages.xlsx file to a pd dataframe:
    log.info(f"Loading the list of sites to scrape in {site_folder}/pages.xlsx.")
    sites_to_scrape_file = f"{site_folder}/pages.xlsx"
    
    try:
        sites_to_scrape_df = pd.read_excel(io = sites_to_scrape_file, 
                                           engine='openpyxl')
    except (FileNotFoundError, IOError) as e:
        log.error(f"Could not find pages.xlsx file in {site_folder}. Skipping site.")
        print(f"Error: Could not find pages.xlsx file in {site_folder}. Skipping site.")
        return
    
    # -- Set the name of the folder to save files to:
    site_output_folder = Path(f"{OUTPUT_DIR}{site_name}")
    
    # -- Check to see if there is a folder in the output directory for the
    # -- site. If not, create it. If so, carry on:
    try:
        site_output_folder.mkdir()
    except FileExistsError:
        pass
    
    
    log.info(f"Folder to save files to has been created. Location is {site_output_folder}.")
    
    # -- Process the URL's in the pages.xlsx file:
    for index, row in sites_to_scrape_df.iterrows():
        # -- Initialise logging:
        log = logging.getLogger(f"{os.getenv('SCRAPER_APP_NAME')}.{__name__}.{inspect.stack()[0][3]}.{site_name}.{row.nickname}")
        
        # -- Setup the settings to use for the scraping:
        browser = row.browser_to_use
        browser_settings = browser_headers_os.loc[(browser_headers_os.browser \
                                                  == browser)].iloc[0]
        
        headers = {"User-Agent": browser_settings.values[2]}
        
        # -- Make a request to the site and process the response with bs:
        log.info(f"Processing scraping of {row.nickname}.")
        
        soup = url_scraper(url = str(row.url), 
                           allowed_http_responses = allowed_http_responses,
                           headers = headers, 
                           parser = "html.parser",
                           nickname = row.nickname,
                           site_name = site_name)
        
        if soup == None:
            return
        
        # -- Import processor module from the current site folder:        
        module_spec = util.spec_from_file_location("processor", 
                                                  f"{site_folder}/processor.py")
        processor_module = util.module_from_spec(module_spec)
        modules["processor"] = processor_module
        module_spec.loader.exec_module(processor_module)

        log.info(f"Passing soup for {row.nickname} to it's processor.")
        # -- Run the soup processor for the page:
        processor_module.process_soup(soup = soup, 
                                      row_details = row,
                                      site_name = site_name,
                                      site_output_folder = site_output_folder)
    
    return