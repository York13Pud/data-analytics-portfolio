# -- Import required libraries / modules:
import logging
import os
import pandas as pd


def process_soup(soup: str, 
                 row_details: pd.DataFrame, 
                 site_output_folder: str):
    """
    ### Summary:
        This function will process a beautiful soup input to output any data that
        the user specifies.

    ### Args:
        soup (str): 
            A beautiful soup object that needs to be processed.
        row_details (dataframe): 
            The row that the page is on. Mainly used for the html id and class tags.
        site_output_folder (str): The path to the output folder for the site.
    ### Returns:
        None
    """
   
    # -- Initialise logging:
    log = logging.getLogger(f"{os.getenv('SCRAPER_APP_NAME')}.{__name__}")
   
    # ==================================================================== #
    # -- Place your code below to process the page into whatever format(s)
    # -- you would like:
    log.info(msg = f"Processing soup for {row_details.nickname}")
    print(f"Page Title: {soup.title}")
    log.info(msg = f"Completed processing soup for {row_details.nickname}")
    
    # ==================================================================== #
    return