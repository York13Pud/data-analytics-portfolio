# -- 0. Import required libraries / modules
from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests
import pandas as pd


# -- 1. Define the URL to scrape:
URL = "https://www.vgchartz.com/charts/platform_totals/Hardware.php"


# -- 2. Perform an HTTPS request to the URL with required headers and store it as a variable:
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0"}
response = requests.get(url = URL, headers = headers)


# -- 3. Extract the HTML from the response:
soup = bs(response.text, "html.parser")


# -- 4. Get the table from the soup (there is only one table on the page):
table = soup.table


# -- 5. Process the contents of the table into two lists. First for the column headers
# ---   and the second for the rows:
column_names = []
table_data = []


# -- Look for rows in the HTML table:
for row in table.find_all('tr'):
    
    # -- Get the column headers:
    for cell in row.find_all('th'):
        column_names.append(cell.text)
    
    # -- Get the data from the rows:
    row_data = []
    
    for cell in row.find_all('td'):
        row_data.append(cell.text)
    
    table_data.append(row_data)


# -- 6. Remove the blank list from the table_data list:
table_data.pop(0)


# -- 7. Create a dataframe from the two lists:
df = pd.DataFrame(table_data, columns = column_names)


# -- 8. Export the contents of the dataframe to a CSV file:
save_to_folder = Path(__file__).resolve().parent
df.to_csv(f"{save_to_folder}/data/01-original-data.csv", index = False)