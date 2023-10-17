# -- Import required libraries / modules:
import inspect
import logging
import os


def replace_chars(text_to_check: str):
    """
    ### Summary:
        This function will take a string and search through it for certain
        characters and replace them with underscores. The characters that will
        be replaces are:
        ' ', '.', ',', '!', '*', '/', '+', ':', ';', '\\', '$', '£', '€', '@'

    ### Args:
        text_to_check (str): 
            A string of text to check and replace characters with underscores.

    ### Returns:
        String (str): 
            A string with the updated text.
    """
    
    # -- Initialise logging:
    log = logging.getLogger(f"{os.getenv('SCRAPER_APP_NAME')}.{__name__}.{inspect.stack()[0][3]}")
    
    log.info(f"Replacing characters in {text_to_check}.")
    
    text_to_replace = [" ", ".", ",", "!", "*", "/", "+", ":", \
                       ";", "\\", "$", "£", "€", "@" ]
    
    for char in text_to_replace:
        new_string = text_to_check.replace(char, "_")
    
    log.info(f"Replacing characters in {text_to_check} completed. New string is {new_string}.")
    
    return str(new_string)