# -- Import required libraries / modules:
from bs4 import BeautifulSoup as bs
from requests import get


def url_scraper(url: str, headers: dict, parser: str = "html.parser"):
    """
    ### Summary:
        This function will scrape a web page and process it using
        BeautifulSoup.
    
    ### Args:
        url (str): The URL that needs to be scraped.
        headers (dict): A dictionary containing the required headers.
        parser (str, optional): The parser that is used to render the web page. 
                                Options are 'html.parser' or 'xml.parser'.
                                Defaults to "html.parser".

    ### Returns:
        object: The processed web page as a BeautifulSoup object.
    """
    
    # -- Make a request to the site:
    response = get(url = url, headers = headers)
        
    # -- Process the response with bs:
    soup = bs(response.text, parser)
    
    return soup