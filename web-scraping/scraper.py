# -- Import required libraries / modules:
from bs4 import BeautifulSoup as bs
from modules.csv_file_actions import read_csv_to_list
from modules.get_os_details import get_os_summary
from pathlib import Path

import requests


# -- Define general constants and variables:
APP_DIR = Path(__file__).resolve().parent
SETTINGS_DIR = "settings"
OS_INFO = get_os_summary()

allowed_http_responses_csv_file = f"{APP_DIR}/{SETTINGS_DIR}/allowed-http-responses.csv"
browser_headers_csv_file = f"{APP_DIR}/{SETTINGS_DIR}/headers.csv"
sites_to_scrape_csv_file = f"{APP_DIR}/{SETTINGS_DIR}/sites.csv"


allowed_http_responses = read_csv_to_list(csv_file_path = str(allowed_http_responses_csv_file), 
                                          skip_headers = bool(1))


print(allowed_http_responses)