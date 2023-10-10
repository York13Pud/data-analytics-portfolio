# -- Import required libraries / modules:
import pandas as pd


def test():
    """
    ### Summary:
        This function will perform a simple print. Only used for testing.
    
    ### Returns:
        Nothing.
    """
    
    print("testing")
    
    return

def process_soup(soup: str, row_details):
    """
    ### Summary:
        This function will process a beautiful soup input to output any data that
        the user specifies.

    ### Args:
        soup (str): A beautiful soup object that needs to be processed.
        row_details: The row that the page is on. Mainly used for the html id and class tags.
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

    df = pd.DataFrame(table_data, columns = column_names)
    print(df.head())
    
    # ==================================================================== #
    return