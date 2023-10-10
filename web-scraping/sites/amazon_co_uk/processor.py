# -- Import required libraries / modules:

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
    
    print(f"Page Title: {soup.title}")
    
    # ==================================================================== #
    return