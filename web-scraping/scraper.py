# -- Import required libraries / modules:
from bs4 import BeautifulSoup as bs
from modules.get_os_details import get_os_summary
from pathlib import Path

import requests
import openpyxl
import pandas as pd


# -- Define general constants and variables:
APP_DIR = Path(__file__).resolve().parent
SETTINGS_DIR = "settings"
OS_INFO = get_os_summary()

allowed_http_responses_file = f"{APP_DIR}/{SETTINGS_DIR}/allowed-http-responses.xlsx"
browser_headers_file = f"{APP_DIR}/{SETTINGS_DIR}/headers.xlsx"
sites_to_scrape_file = f"{APP_DIR}/{SETTINGS_DIR}/sites.xlsx"


allowed_http_responses = pd.read_excel(io = allowed_http_responses_file)
print(allowed_http_responses.head())

browser_headers_df = pd.read_excel(io = browser_headers_file)
#(filepath_or_buffer = browser_headers_csv_file)
browser_headers_df = browser_headers_df.loc[(browser_headers_df.os == OS_INFO["os_type"]) & \
                     (browser_headers_df.browser == "firefox")]

print(browser_headers_df.user_agent.values)

sites_to_scrape_df = pd.read_excel(io = sites_to_scrape_file)
print(sites_to_scrape_df.head())