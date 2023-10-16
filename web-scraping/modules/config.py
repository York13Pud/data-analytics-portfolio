# -- Import required libraries / modules:
from pathlib import Path

import logging
import logging.config


# -- Define general constants and variables:
# -- Folders for various settings:
APP_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = f"{APP_DIR}/logs/"
OUTPUT_DIR = f"{APP_DIR}/output/"
SETTINGS_DIR = f"{APP_DIR}/settings/"

ALL_SITES_DIR = f"{APP_DIR}/sites/"
SITE_FILES = ["pages.xlsx", "processor.py"]


# -- Setup logging settings:
def logger(name: str, log_folder: str):
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'console': {
                'format': '%(levelname)s:%(asctime)s:%(name)s:%(message)s'
            },
            'file': {
                'format': '%(levelname)s:%(asctime)s:%(name)s:%(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'formatter': 'file',
                'filename': log_folder
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['file'],
                'propagate': True,
            }
        }
    })

    return logging.getLogger(name)