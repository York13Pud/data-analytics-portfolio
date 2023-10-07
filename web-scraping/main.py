# -- Import required libraries / modules:
from bs4 import BeautifulSoup as bs
from importlib import util
from modules.get_os_details import get_os_summary
from pathlib import Path
from sys import modules

import pandas as pd

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

    # -- To-do: Add error checking. After that is done, add logging.

    # -- Import settings from excel files:
    # -- HTTP responses:
    allowed_http_responses_file = f"{SETTINGS_DIR}allowed-http-responses.xlsx"
    allowed_http_responses = pd.read_excel(io = allowed_http_responses_file)


    # -- Web browser headers:
    browser_headers_file = f"{SETTINGS_DIR}headers.xlsx"
    browser_headers_df = pd.read_excel(io = browser_headers_file)


    # -- Filter the browser_header_df for the O/S:
    browser_headers_df = browser_headers_df.loc[\
                                (browser_headers_df.os == OS_INFO["os_type"])
                                ]


    # --------------------------------------------------------------------------- #
    # --------------------------------------------------------------------------- #

    # -- To-do: Change sites to check to process excel files in settings/sites.

    for folder in SITE_FOLDER_CONTENTS:
        # -- Check if pages and processor files are files:
        pages_file = Path(f"{folder}/{SITE_FILES[0]}").is_file()
        processor_file = Path(f"{folder}/{SITE_FILES[1]}").is_file()
            
        print("\n=================================================================")
        print(f"Folder: {folder}")
        
        # -- Check if pages and processor files are present or not:
        if pages_file == True and processor_file == True:
            # -- To-do: Import module, read xlsx, scrape, soup and export.
            print("Files are present")
            # -- Load processor:
            # -- Import processor module from the current folder:
            module_spec = util.spec_from_file_location("processor", f"{folder}/processor.py")
            processor_module = util.module_from_spec(module_spec)
            modules["processor"] = processor_module
            module_spec.loader.exec_module(processor_module)
                    
            # -- Execute the processor:
            processor_module.testing_things()

        else:
            # -- To-do: Generate error.
            print("\n--- Error ---")
            print(f"pages.xlsx present: {pages_file}")
            print(f"processor.py present: {processor_file}")
            print("\nPlease check that the files showing as False are present.")

    """
    1. For loop to go over folders in SITES_DIR.
    2. Check if pages and processor are present.
    3. If both are true, load the processor module.
    4. Processor does its job.

    """

# Run the program:
if __name__ == "__main__":
    main()