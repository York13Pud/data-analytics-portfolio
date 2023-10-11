# -- Import required libraries / modules:
from bs4 import BeautifulSoup as bs
from importlib import util
from requests import get
from sys import modules

import pandas as pd


def url_scraper(url: str,
                allowed_http_responses: list, 
                headers: dict, 
                parser: str = "html.parser"):
    """
    ### Summary:
        This function will scrape a web page and process it using
        BeautifulSoup.
    
    ### Args:
        url (str): The URL that needs to be scraped.
        allowed_http_responses (dataframe): A dataframe with a list of HTTP responses.
        headers (dict): A dictionary containing the required headers.
        parser (str, optional): The parser that is used to render the web page. 
                                Options are 'html.parser' or 'xml.parser'.
                                Defaults to "html.parser".
        
        
    ### Returns:
        object: The processed web page as a BeautifulSoup object.
    """
    
    # -- Make a request to the site:
    response = get(url = url, headers = headers)
    
    if response.status_code in allowed_http_responses:
        # -- Process the response with bs:
        soup = bs(response.text, parser)    
        return soup
    else:
        print("404")
        return
        

def processor(allowed_http_responses,
              browser_headers_os,
              output_folder: str,
              site_folder: str):

    # -- Load the contents of the pages.xlsx file to a pd dataframe:
    sites_to_scrape_file = f"{site_folder}/pages.xlsx"
    sites_to_scrape_df = pd.read_excel(io = sites_to_scrape_file, 
                                       engine='openpyxl')
   
    # -- Process the URL's in the pages.xlsx file:
    for index, row in sites_to_scrape_df.iterrows():
        # -- Setup the settings to use for the scraping:
        browser = row.browser_to_use
        browser_settings = browser_headers_os.loc[(browser_headers_os.browser \
                                                  == browser)].iloc[0]
        headers = {"User-Agent": browser_settings.values[2]}
        
        # -- Make a request to the site and process the response with bs:
        soup = url_scraper(url = str(row.url), 
                           headers = headers, 
                           parser = "html.parser",
                           allowed_http_responses = allowed_http_responses)
                       
        # -- Import processor module from the current site folder:
                
        module_spec = util.spec_from_file_location("processor", 
                                                  f"{site_folder}/processor.py")
        processor_module = util.module_from_spec(module_spec)
        modules["processor"] = processor_module
        module_spec.loader.exec_module(processor_module)

        # -- Run the soup processor for the page:
        processor_module.process_soup(soup = soup, 
                                      row_details = row,
                                      output_folder = output_folder)
        
        # ==================================================================== #
    
    return