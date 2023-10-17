# -- Version 1.0
# -- Created by: dev_neil_a
# -- Created: 2023-10-02
# -- Updated: 2023-10-02


# -- Import required libraries / modules:
from modules.config import logger, LOGS_DIR

import platform


def get_os_summary():
    """
    ### Summary: 
        This will get a collection of details about the system it's being run on.
    
    ### Parameters: 
        None required.

    ### Returns:
        dict: 
            hostname (str): 
                The O/S name (linux, macos or windows) (lowercase).
            os_type (str): 
                The system name (lowercase).
            os_version (str): 
                O/S release version (lowercase).
            os_arch (str): 
                The CPU architecture of the system (lowercase).
            cpu_arch (str): 
                The O/S architecture (32bit or 64bit) (lowercase).
    """
    
    # -- Initialise logging:
    log = logger(name = __name__, log_folder = f"{LOGS_DIR}/main.log")
    
    log.info("Collecting operating system information")
    
    # -- Check the O/S name and if it is Darwin, change it to macos.
    # -- Linux and windows don't need any other changes.
    if platform.system() == "Darwin":
        os_name = "macos".lower()
        os_release = platform.mac_ver()[0].lower()
    else:
        os_name = platform.system().lower()
        os_release = platform.release().lower()

    # -- Create a dictionary with the O/S details in: 
    os_details = {
        "hostname": str(platform.node().lower()), 
        "os_type": str(os_name.lower()), 
        "os_version": str(os_release.lower()), 
        "os_arch": str(platform.architecture()[0].lower()),
        "cpu_arch": str(platform.machine().lower())
    }
    
    log.info(f"O/S details: {os_details}")
    
    log.info(f"Collecting operating system information completed")
    
    # --- Return the details about the O/S / system:
    return os_details