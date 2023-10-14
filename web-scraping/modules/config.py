# -- Import required libraries / modules:
from pathlib import Path

import logging


# -- Define general constants and variables:
# -- Folders for various settings:
APP_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = f"{APP_DIR}/logs/"
OUTPUT_DIR = f"{APP_DIR}/output/"
SETTINGS_DIR = f"{APP_DIR}/settings/"

ALL_SITES_DIR = f"{APP_DIR}/sites/"
SITE_FILES = ["pages.xlsx", "processor.py"]


# -- Setup logging settings: