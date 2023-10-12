def replace_chars(text_to_check: str):
    """
    ### Summary:
        This function will take a string and search through it for certain
        characters and replace them with underscores. The characters that will
        be replaces are:
        ' ', '.', ',', '!', '*', '/', '+', ':', ';', '\\', '$', '£', '€', '@'

    ### Args:
        text_to_check (str): A string of text to check and replace characters 
        with underscores.

    ### Returns:
        string: A string with the 
    """
    text_to_replace = [" ", ".", ",", "!", "*", "/", "+", ":", \
                       ";", "\\", "$", "£", "€", "@" ]
    
    for char in text_to_replace:
        string = text_to_check.replace(char, "_")
    
    return str(string)