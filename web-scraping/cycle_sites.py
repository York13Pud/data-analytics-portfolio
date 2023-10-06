# -- The sites to scrape and the browser to use:
sites_to_scrape_file = f"{SETTINGS_DIR}sites.xlsx"
sites_to_scrape_df = pd.read_excel(io = sites_to_scrape_file)


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
    
    
    column_names = []
    table_data = []
        
    table = soup.find("table", attrs = table_attributes)
    
        
    # -- Look for rows in the HTML table:
    for item in table.find_all('tr'):
        
        # -- Get the column headers:
        for cell in item.find_all('th'):
            column_names.append(cell.text)
        
        # -- Get the data from the rows:
        row_data = []
        
        for cell in item.find_all('td'):
            print(cell.text)
            row_data.append(cell.text)
                
        table_data.append(row_data)


    # -- 6. Remove the blank list from the table_data list:
    table_data.pop(0)

    # -- 7. Create a dataframe from the two lists:
    df = pd.DataFrame(table_data, columns = column_names)

    # -- 8. Export the contents of the dataframe to an Excel file:
    save_to_folder = Path(__file__).resolve().parent
    # df.to_csv(f"{save_to_folder}/01-original-data.csv", index = False)