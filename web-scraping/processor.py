from importlib import util
from pathlib import Path
from sys import modules


def process_scraping():
    pass

SITE_FOLDER_PATH = "/Users/neil/Documents/training/data-analytics/data-analytics-portfolio/web-scraping/sites/"
SITE_FOLDER_CONTENTS = list(Path(SITE_FOLDER_PATH).iterdir())
FILES = ["pages.xlsx", "processor.py"]
# SITE_FOLDER_MODULE_PATH = ".sites"


for folder in SITE_FOLDER_CONTENTS:
    # -- Check if pages and processor files are files:
    pages_file = Path(f"{folder}/{FILES[0]}").is_file()
    processor_file = Path(f"{folder}/{FILES[1]}").is_file()
           
    print("\n=================================================================")
    print(f"Folder: {folder}")
    
    # -- Check if pages and processor files are present or not:
    if pages_file == True and processor_file == True:
        # -- To-do: Import module, read xlsx, scrape, soup and export.
        print("Files are present")
        # -- Load processor:
        # -- Import processor module from the current folder:
        module_spec = util.spec_from_file_location("processor", f"{folder}/processor.py")
        processor_module = util.module_from_spec(module_spec)
        modules["processor"] = processor_module
        module_spec.loader.exec_module(processor_module)
                
        # -- Execute the processor:
        processor_module.testing_things()

    else:
        # -- To-do: Generate error.
        print("\n--- Error ---")
        print(f"pages.xlsx present: {pages_file}")
        print(f"processor.py present: {processor_file}")
        print("\nPlease check that the files showing as False are present.")
          
        
# fs = str(file_name).rsplit('/', 1)
# fn = str(fs[1]).split('.', 1)
# fr = str(file_name).replace(',', '_')
# print(f"--- File: {fr}")