# -- To-do: Add date to the file name.
# -- To-do: Build file name based on site, date and time.

def export_to_csv(df,  filepath:str, filename:str):
    df.to_csv(f"{save_to_folder}/01-original-data.csv", index = False)
    
    
def export_to_excel(df, filepath:str, filename:str):
    df.to_excel(excel_writer=f"{save_to_folder}/01-original-data.xlsx", 
                index = False)