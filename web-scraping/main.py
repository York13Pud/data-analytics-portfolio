# -- Import required libraries / modules:
from datetime import datetime
from pathlib import Path

from modules.config import ALL_SITES_DIR, LOGS_DIR, OUTPUT_DIR, SETTINGS_DIR, logger
from modules.get_os_details import get_os_summary
from modules.scraper import processor

import inspect
import os
import pandas as pd


def main():
    """
    ### Summary:
        This is the main entry point into the program. It will:
        - Define the constants and variables that are shared throughout the
          program.
        - Gather the operating system information. This is used for filtering 
          which web browser and settings to use for scraping later on.
        - Cycle through the sites folder and run actions against each folders
          contents.
    
    ### Args:
        None.
    
    ### Returns:
        None.
    """
    
    # -- Create logging folder:
    TODAYS_LOGS_DIR = Path(f"{LOGS_DIR}/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}")
    
    try:
        TODAYS_LOGS_DIR.mkdir(parents = True)
    except FileExistsError:
        pass
    
    # -- Create environment variable for todays logs folder:
    os.environ['TODAYS_LOGS_DIR'] = str(TODAYS_LOGS_DIR)
    
    # -- Create environment variable for todays logs folder:
    os.environ['SCRAPER_APP_NAME'] = str("scraper")
    
    # -- Initialise logging:
    log_main = logger(name = f"{os.getenv('SCRAPER_APP_NAME')}.main.{inspect.stack()[0][3]}", 
                      log_folder = f"{os.getenv('TODAYS_LOGS_DIR')}/main.log")
            
    log_main.info("===== Starting program =====")
    
    # -- Set the name of the folder to save files to:
    output_folder = Path(f"{OUTPUT_DIR}")
    
    # -- Check to see if there is a folder for the output directory.
    # -- If not, create it. If so, carry on:
    try:
        output_folder.mkdir(parents = True)
    except FileExistsError:
        pass
    
    # -- Define general constants and variables:
    # -- Folders for various settings:
    SITE_FILES = ["pages.xlsx", "processor.py"]
    
    # -- Create a list of all the sub-folders in ALL_SITES_DIR.
    log_main.info(f"Collecting sites list from {ALL_SITES_DIR}.")
    
    SITE_FOLDER_CONTENTS = [folder_name for folder_name in \
                            Path(ALL_SITES_DIR).iterdir() \
                            if not folder_name.name.startswith(".") \
                            if folder_name.is_dir()]

    # -- Import settings from excel files:
    # -- HTTP responses:
    allowed_http_responses_file = f"{SETTINGS_DIR}allowed-http-responses.xlsx"
    log_main.info(f"Loading allowed-http-responses.xlsx in {SETTINGS_DIR}.")
    
    try:
        allowed_http_responses_df = pd.read_excel(io = allowed_http_responses_file)
    except (FileNotFoundError, IOError) as e:
        log_main.error(f"Could not find allowed-http-responses.xlsx file in {SETTINGS_DIR}. Exiting the program.")
        print(f"Error: Could not find allowed-http-responses.xlsx file in {SETTINGS_DIR}. Exiting the program.")
        return

    log_main.info(f"Loading allowed-http-responses.xlsx in {SETTINGS_DIR} completed.")
    
    # -- Web browser headers:
    browser_headers_file = f"{SETTINGS_DIR}headers.xlsx"
    log_main.info(f"Loading headers.xlsx in {SETTINGS_DIR}.")
    
    try:
        browser_headers_df = pd.read_excel(io = browser_headers_file)
    except (FileNotFoundError, IOError) as e:
        log_main.error(f"Could not find headers.xlsx file in {SETTINGS_DIR}. Exiting the program.")
        print(f"Error: Could not find headers.xlsx file in {SETTINGS_DIR}. Exiting the program.")
        return
        

    log_main.info(f"Loading headers.xlsx in {SETTINGS_DIR} completed.")

    # -- Collect info about the Operating System the program is running on:
    log_main.info("Collecting Operating System Information.")
    OS_INFO = get_os_summary()

    # -- Cycle through the folders in SITE_FOLDER_CONTENTS:
    for folder in SITE_FOLDER_CONTENTS:
        # -- Check if pages and processor files are files (True or False):
        pages_file = Path(f"{folder}/{SITE_FILES[0]}").is_file()
        processor_file = Path(f"{folder}/{SITE_FILES[1]}").is_file()
        
        log_main.info(f"Checking that {SITE_FILES[0]} and {SITE_FILES[1]} are present in {folder}.")
        
        # -- Check if pages and processor files are present or not:
        if pages_file == True and processor_file == True:
            log_main.info(f"{SITE_FILES[0]} and {SITE_FILES[1]} are present in {folder}.")
            log_main.info(f"Executing scraping and processing of sites in {folder}/{SITE_FILES[0]}.")            
            
            # -- Execute the processor:
            processor(browser_headers_os = browser_headers_df.loc[\
                                (browser_headers_df.os == OS_INFO["os_type"])],
                      allowed_http_responses = allowed_http_responses_df.values,
                      site_folder = folder)

        else:
            if pages_file == False:
                log_main.error(f"{SITE_FILES[0]} could not be found in {folder}.")
            if pages_file == False:
                log_main.error(f"{SITE_FILES[1]} could not be found in {folder}.")
            
            log_main.warning(f"Check that {SITE_FILES[0]} and {SITE_FILES[1]} are present in {folder}.")
            log_main.warning(f"Skipping processing {folder}.")

    # -- Complete the program:
    log_main.info("===== Stopping program =====")
    
    return

# Run the program:
if __name__ == "__main__":
    main()