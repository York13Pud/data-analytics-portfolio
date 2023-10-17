# -- Import required libraries / modules:
from modules.config import logger, LOGS_DIR

import pandas as pd


def export_to_csv(df: pd.DataFrame, 
                  filepath:str, 
                  filename:str,
                  nickname: str):
    """
    ### Summary:
        This function will export a pandas dataframe to a CSV file using the
        filepath and filename provided.

    ### Args:
        df (pd.DataFrame):
            The dataframe that needs to be exported.
        filepath (str):
            The path that the file needs to saved to.
        filename (str):
            The name of the file to use.
        nickname (str):
            The nickname of the site that is being scraped.
                
    ### Returns:
        None
    """
    # -- Create a new logger:
    log = logger(name = f"{__name__}.{nickname}", log_folder = f"{LOGS_DIR}/main.log")
    
    log.info(f"Saving to {filename}.csv in {filepath}")
    
    # -- Attempt to save the file:
    try:
        df.to_csv(f"{filepath}/{filename}.csv", 
                  index = False)
    except FileNotFoundError:
        log.error(f"Unable to save {filename}.csv in {filepath}. Please check that the location is valid.")

    return
    
def export_to_excel(df: pd.DataFrame, 
                    filepath: str, 
                    filename: str,
                    nickname: str):
    """
    ### Summary:
        This function will export a pandas dataframe to an Excel file using the
        filepath and filename provided.

    ### Args:
        df (pd.DataFrame):
            The dataframe that needs to be exported.
        filepath (str):
            The path that the file needs to saved to.
        filename (str):
            The name of the file to use.
        nickname (str):
            The nickname of the site that is being scraped.
            
    ### Returns:
        None
    """
    # -- Create a new logger:
    log = logger(name = f"{__name__}.{nickname}", log_folder = f"{LOGS_DIR}/main.log")
    
    log.info(f"Saving to {filename}.xlsx in {filepath}")
    
    # -- Attempt to save the file:
    try:
        df.to_excel(excel_writer=f"{filepath}/{filename}.xlsx", 
                    index = False)
    except FileNotFoundError:
        log.error(f"Unable to save {filename}.xlsx in {filepath}. Please check that the location is valid.")
    
    return