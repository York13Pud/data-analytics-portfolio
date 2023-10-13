# -- Import required libraries / modules:
from datetime import datetime
from pathlib import Path

from modules.export_files import export_to_excel

import pandas as pd


def process_soup(soup: str, 
                 row_details: pd.DataFrame, 
                 site_output_folder: str):
    """
    ### Summary:
        This function will process a beautiful soup input to output any data that
        the user specifies.

    ### Args:
        soup (str): 
            A beautiful soup object that needs to be processed.
        row_details (dataframe): 
            The row that the page is on. Mainly used for the html id and class tags.
        site_output_folder (str): The path to the output folder for the site.
    ### Returns:
        None
    """
    
    # ==================================================================== #
    # -- Place your code below to process the page into whatever format(s)
    # -- you would like:
    
    # -- Construct the attributes to use to find the table:
    table_attributes = {}
    
    # -- Check if both an id and a class have been specified for the site.
    # -- If not, don't add them to the table_attributes dict:
    if pd.isna(row_details.html_id_1):
        print("No HTML 'id' tag specified.")
    else:
        table_attributes.update({"id": row_details.html_id_1})
        
    if pd.isna(row_details.html_class_1):
        print("No HTML / CSS 'class' tag specified.")
    else:
        table_attributes.update({"class": row_details.html_class_1})
    
    # -- Check if table attributes is empty or not:
    if table_attributes == {}:
        # -- To-do: Raise warning that nothing was supplied and page skipped:
        print("Nothing to do as no id or class tags have been supplied.")
        return
    else:
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
                row_data.append(cell.text)
                    
            table_data.append(row_data)        

        # -- To-do: Check for empty row and if found delete them.
        # -- Remove the blank list from the table_data list:
        table_data.pop(0)
        
        # -- Create a dataframe from the column_names and table_data lists:
        df = pd.DataFrame(table_data, columns = column_names)
        
        # -- Create the output folder(s) as needed and then save the df to an
        # -- Excel file:
        todays_date = datetime.now().date()
        current_time = datetime.now().time()
        
        site_output_folder_full_path = Path(str(f"{site_output_folder}/{todays_date.year}/{todays_date.month}/{todays_date.day}/"))
               
        try:
            site_output_folder_full_path.mkdir(parents = True)
        except FileExistsError:
            pass
        
        # -- Export df to an Excel file:
        export_to_excel(df = df, 
                        filepath = site_output_folder_full_path, 
                        filename = str(f"{todays_date}-{current_time}-{row_details.nickname}")) 
         
        # ==================================================================== #
        return