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


# -- Import settings from excel files:
# -- HTTP responses:
allowed_http_responses_file = f"{APP_DIR}/{SETTINGS_DIR}/allowed-http-responses.xlsx"
allowed_http_responses = pd.read_excel(io = allowed_http_responses_file)


# -- Web browser headers:
browser_headers_file = f"{APP_DIR}/{SETTINGS_DIR}/headers.xlsx"
browser_headers_df = pd.read_excel(io = browser_headers_file)


# -- Filter the browser_header_df for the os and chosen browser:
browser_headers_df = browser_headers_df.loc[\
                            (browser_headers_df.os == OS_INFO["os_type"])
                            ]


# -- The sites to scrape and the browser to use:
sites_to_scrape_file = f"{APP_DIR}/{SETTINGS_DIR}/sites.xlsx"
sites_to_scrape_df = pd.read_excel(io = sites_to_scrape_file)
#sites_to_scrape_df.

# Perform web scraping:
for index, row in sites_to_scrape_df.iterrows():
    # -- Setup the settings to use for the scraping:
    browser = row.browser_to_use
    browser_settings = browser_headers_df.loc[(browser_headers_df.browser == browser)].iloc[0]
    headers = {"User-Agent": browser_settings.values[2]}
    
    # -- Make a request to the site:
    response = requests.get(url = row.url, headers = headers)
    
    # -- Process the response with bs:
    soup = bs(response.text, "html.parser")
    
    # -- Construct the attributes to use to find the table:
    table_attributes = {}
     
    # -- Check if both an id and a class have been specified for the site.
    # -- If not, don't add them to the table_attributes dict:
    if pd.isna(row.table_id):
        pass
    else:
        table_attributes.update({"id": row.table_id})
        
    if pd.isna(row.table_class):
        pass
    else:
        table_attributes.update({"class": row.table_class})
    
    print(soup.title.text)
    print(soup.h1.text)
    print(soup.find_all("table", attrs = table_attributes))

    # with open("./html.txt", "w") as output:
    #     output.write(response.text)