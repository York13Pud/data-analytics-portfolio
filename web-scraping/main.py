# -- Import required libraries / modules:
from pathlib import Path

from modules.get_os_details import get_os_summary
from modules.scraper import processor

import pandas as pd

# -- To-do: Add error checking. After that is done, add logging.

def main():
    # -- Define general constants and variables:
    # -- Folders for various settings:
    APP_DIR = Path(__file__).resolve().parent
    LOGS_DIR = f"{APP_DIR}/logs/"
    SETTINGS_DIR = f"{APP_DIR}/settings/"

    ALL_SITES_DIR = f"{APP_DIR}/sites/"
    SITE_FILES = ["pages.xlsx", "processor.py"]
    SITE_FOLDER_CONTENTS = list(Path(ALL_SITES_DIR).iterdir())

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

    # -- To-do: Change sites to check to process excel files in settings/sites.

    # -- Cycle through the folders in SITE_FOLDER_CONTENTS:
    for folder in SITE_FOLDER_CONTENTS:
        # -- Check if pages and processor files are files:
        pages_file = Path(f"{folder}/{SITE_FILES[0]}").is_file()
        processor_file = Path(f"{folder}/{SITE_FILES[1]}").is_file()
            
        print("\n=============================================================")
        print(f"Folder: {folder}")
        
        # -- Check if pages and processor files are present or not:
        if pages_file == True and processor_file == True:
            # -- To-do: Import module, read xlsx, scrape, soup and export.
            print("Files are present")
            
            # -- Execute the processor:
            processor(\
                browser_headers_os = browser_headers_df.loc[\
                                (browser_headers_df.os == OS_INFO["os_type"])],
                allowed_http_responses = allowed_http_responses_df.values,
                site_folder = folder)

        else:
            # -- To-do: Generate error.
            print("\n--- Error ---")
            print(f"pages.xlsx present: {pages_file}")
            print(f"processor.py present: {processor_file}")
            print("\nPlease check that the files showing as False are present.")


# Run the program:
if __name__ == "__main__":
    main()