# -- Import required libraries / modules:
from bs4 import BeautifulSoup as bs
from modules.get_os_details import get_os_summary
from pathlib import Path

import pandas as pd
import requests


# -- Define general constants and variables:
# -- Folders for various settings:
APP_DIR = Path(__file__).resolve().parent
LOGS_DIR = f"{APP_DIR}/logs/"
SETTINGS_DIR = f"{APP_DIR}/settings/"
SITES_DIR = f"{APP_DIR}/sites/"
SITE_FOLDER_PATH = "/Users/neil/Documents/training/data-analytics/data-analytics-portfolio/web-scraping/sites/"
SITE_FOLDER_CONTENTS = list(Path(SITE_FOLDER_PATH).iterdir())
FILES = ["pages.xlsx", "processor.py"]



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










