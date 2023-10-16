# -- Import required libraries / modules:
from datetime import datetime
from pathlib import Path

from modules.config import logger, LOGS_DIR

import inspect
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
    
    # -- Initialise logging configuration:
    site_log_folder = str(Path(__file__).resolve().parent).rsplit('/', 1)
    site_log_folder_full_path = f"{LOGS_DIR}{site_log_folder[1]}"
    
    # try:
    #     Path(str(site_log_folder_full_path)).mkdir(parents = True)
    # except FileExistsError:
    #     pass   
    
    log = logger(name = f"sites.{site_log_folder[1]}.{__name__}.{inspect.stack()[0][3]}.{str(row_details.nickname).lower()}", log_folder = f"{LOGS_DIR}main.log")
    
    # ==================================================================== #
    # -- Place your code below to process the page into whatever format(s)
    # -- you would like:
    log.info(msg = f"Processing soup for {row_details.nickname}")
    print(f"Page Title: {soup.title}")
    log.info(msg = f"Completed processing soup for {row_details.nickname}")
    
    # ==================================================================== #
    return