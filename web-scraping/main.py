# -- Import required libraries / modules:
from pathlib import Path

from modules.get_os_details import get_os_summary
from modules.scraper import processor

import pandas as pd
from modules.config import ALL_SITES_DIR, LOGS_DIR, OUTPUT_DIR, SETTINGS_DIR


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
    
    # -- Define general constants and variables:
    # -- Folders for various settings:
    SITE_FILES = ["pages.xlsx", "processor.py"]
    
    # -- Create a list of all the sub-folders in ALL_SITES_DIR.
    SITE_FOLDER_CONTENTS = [folder_name for folder_name in \
                            Path(ALL_SITES_DIR).iterdir() \
                            if not folder_name.name.startswith(".") \
                            if folder_name.is_dir()]
    
    # -- Collect info about the Operating System the program is running on:
    OS_INFO = get_os_summary()

    # -- Import settings from excel files:
    # -- HTTP responses:
    allowed_http_responses_file = f"{SETTINGS_DIR}allowed-http-responses.xlsx"
    allowed_http_responses_df = pd.read_excel(io = allowed_http_responses_file)

    # -- Web browser headers:
    browser_headers_file = f"{SETTINGS_DIR}headers.xlsx"
    browser_headers_df = pd.read_excel(io = browser_headers_file)

    # ------------------------------------------------------------------------ #

    # -- Cycle through the folders in SITE_FOLDER_CONTENTS:
    for folder in SITE_FOLDER_CONTENTS:
        # -- Check if pages and processor files are files (True or False):
        pages_file = Path(f"{folder}/{SITE_FILES[0]}").is_file()
        processor_file = Path(f"{folder}/{SITE_FILES[1]}").is_file()
            
        print("\n=============================================================")
        print(f"Folder: {folder}")
        
        # -- Check if pages and processor files are present or not:
        if pages_file == True and processor_file == True:
            print("Files are present")
            
            # -- Execute the processor:
            processor(\
                browser_headers_os = browser_headers_df.loc[\
                                (browser_headers_df.os == OS_INFO["os_type"])],
                allowed_http_responses = allowed_http_responses_df.values,
                output_folder = OUTPUT_DIR,
                site_folder = folder)

        else:
            # -- To-do: Generate error and log.
            print("\n--- Error ---")
            print(f"pages.xlsx present: {pages_file}")
            print(f"processor.py present: {processor_file}")
            print("\nPlease check that the files showing as False are present.")
    
    return

# Run the program:
if __name__ == "__main__":
    main()