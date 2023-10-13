# -- Version 1.0
# -- Created by: dev_neil_a
# -- Created: 2023-10-02
# -- Updated: 2023-10-02


# -- Import required libraries / modules:
import platform


def get_os_summary():
    """
    ### Summary: 
        This will get a collection of details about the system it's being run on.
    
    ### Parameters: 
        None required.

    ### Returns:
        dict: 
            hostname (String): 
                The O/S name (linux, macos or windows) (lowercase).
            os_type (String): 
                The system name (lowercase).
            os_version (String): 
                O/S release version (lowercase).
            os_arch (String): 
                The CPU architecture of the system (lowercase).
            cpu_arch (String): 
                The O/S architecture (32bit or 64bit) (lowercase).
    """
    
    # --- Check the O/S name and if it is Darwin, change it to macos.
    # --- Linux and windows don't need any other changes.
    if platform.system() == "Darwin":
        os_name = "macos".lower()
        os_release = platform.mac_ver()[0].lower()
    else:
        os_name = platform.system().lower()
        os_release = platform.release().lower()

    # --- Return the details about the O/S / system:
    return {
        "hostname": str(platform.node().lower()), 
        "os_type": str(os_name.lower()), 
        "os_version": str(os_release.lower()), 
        "os_arch": str(platform.architecture()[0].lower()),
        "cpu_arch": str(platform.machine().lower())
    }