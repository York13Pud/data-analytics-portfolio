# -- Import required libraries / modules:
import pandas as pd


def export_to_csv(df: pd.DataFrame, 
                  filepath:str, 
                  filename:str):
    """
    ### Summary:
        This function will export a pandas dataframe to a CSV file using the
        filepath and filename provided.

    ### Args:
        df (pd.DataFrame):
            The dataframe that needs to be exported.
        filepath (str):
            The path that the file needs to saved to.
        filename (str):
            The name of the file to use.
    
    ### Returns:
        None
    """
    df.to_csv(f"{filepath}/{filename}.csv", 
        index = False)
    
    return
    
def export_to_excel(df: pd.DataFrame, 
                    filepath:str, 
                    filename:str):
    """
    ### Summary:
        This function will export a pandas dataframe to an Excel file using the
        filepath and filename provided.

    ### Args:
        df (pd.DataFrame):
            The dataframe that needs to be exported.
        filepath (str):
            The path that the file needs to saved to.
        filename (str):
            The name of the file to use.
    
    ### Returns:
        None
    """
    
    df.to_excel(excel_writer=f"{filepath}/{filename}.xlsx", 
                index = False)
    return