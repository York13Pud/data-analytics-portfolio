# -- Import required libraries / modules:
from bs4 import BeautifulSoup as bs
from modules.get_os_details import get_os_summary
from pathlib import Path

import pandas as pd
import requests


# -- Define general constants and variables:
APP_DIR = Path(__file__).resolve().parent
SETTINGS_DIR = "settings"
OS_INFO = get_os_summary()


allowed_http_responses_file = f"{APP_DIR}/{SETTINGS_DIR}/allowed-http-responses.xlsx"
allowed_http_responses = pd.read_excel(io = allowed_http_responses_file)


browser_headers_file = f"{APP_DIR}/{SETTINGS_DIR}/headers.xlsx"
browser_headers_df = pd.read_excel(io = browser_headers_file)

# -- Filter the browser_header_df for the os and chosen browser:
browser_headers_df = browser_headers_df.loc[\
                            (browser_headers_df.os == OS_INFO["os_type"]) & \
                            (browser_headers_df.browser == "firefox")
                            ]

# print(browser_headers_df.user_agent.values)

sites_to_scrape_file = f"{APP_DIR}/{SETTINGS_DIR}/sites.xlsx"
sites_to_scrape_df = pd.read_excel(io = sites_to_scrape_file)
