# -- Version 1.0
# -- Created by: dev_neil_a
# -- Created: 2023-10-03
# -- Updated: 2023-10-03


# -- Import required libraries / modules:
import csv


def read_csv_to_list(csv_file_path:str, skip_headers:bool = 0):
    """
    ### Summary:
        This function will take a CSV file and return the contents back as a list.
        
    ### Arguments:
        csv_file_path (str): 
            The full path and name of the CSV file to use.
        skip_headers (bool, optional) Default = 0: 
            Allows for the first row to be skipped. 0 = Don't skip, 1 = Skip. 
            
    ### Returns:
        list:
            Each item added to the list is returned as a string.
    """

    # --- Create an empty list:
    csv_content = list()
    
    # -- Read the CSV file provided:
    with open(file = csv_file_path, mode = "r") as csv_file:    
        csv_reader = csv.reader(csv_file)
    
        # -- Check to see if the headers (first row) needs to be skipped.
        # -- 0 = Don't skip, 1 = Skip.
        if skip_headers == 1:
            next(csv_reader)
            
        # -- Add the rows in csv_reader to the list
        for row in csv_reader:
            csv_content += (row)
    
    # -- Return the contents of the CSV file:
    return csv_content