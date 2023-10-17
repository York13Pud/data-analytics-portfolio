# -- Import required libraries / modules:
import inspect
import logging
import os
import pandas as pd


def export_to_csv(df: pd.DataFrame, 
                  filepath:str, 
                  filename:str,
                  nickname: str,
                  site_name: str):
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
        site_name (str):
            The name of the site folder that is used.
                
    ### Returns:
        None
    """
    
    # -- Initialise logging:
    log = logging.getLogger(f"{os.getenv('SCRAPER_APP_NAME')}.{__name__}.{inspect.stack()[0][3]}.{site_name}.{nickname}")
    
    log.info(f"Saving to {filename}.csv in {filepath}.")
    
    # -- Attempt to save the file:
    try:
        df.to_csv(f"{filepath}/{filename}.csv", 
                  index = False)
    except (FileNotFoundError, IOError) as e:
        log.error(f"Unable to save {filename}.csv in {filepath}. Please check that the location is valid.")
        print(f"Unable to save {filename}.csv in {filepath}. Please check that the location is valid.")
        return
    
    log.info(f"File has been saved. The file can be found at {filepath}/{filename}.csv.")
    
    return
 
   
def export_to_excel(df: pd.DataFrame, 
                    filepath: str, 
                    filename: str,
                    nickname: str,
                    site_name: str):
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
        site_name (str):
            The name of the site folder that is used.
    ### Returns:
        None
    """
    
    # -- Initialise logging:
    log = logging.getLogger(f"{os.getenv('SCRAPER_APP_NAME')}.{__name__}.{inspect.stack()[0][3]}.{site_name}.{nickname}")
    
    log.info(f"Saving to {filename}.xlsx in {filepath}.")
    
    # -- Attempt to save the file:
    try:
        df.to_excel(excel_writer=f"{filepath}/{filename}.xlsx", 
                    index = False)
    except (FileNotFoundError, IOError) as e:
        log.error(f"Unable to save {filename}.xlsx in {filepath}. Please check that the location is valid.")
        print(f"Unable to save {filename}.xlsx in {filepath}. Please check that the location is valid.")
        return
    
    log.info(f"File has been saved. The file can be found at {filepath}/{filename}.xlsx.")
    
    return