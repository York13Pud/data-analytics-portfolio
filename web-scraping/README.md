# Multi-Site Web Scraper

## Table of Contents

- [Multi-Site Web Scraper](#multi-site-web-scraper)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [pages.xlsx](#pagesxlsx)
    - [processor.py](#processorpy)
    - [Other Folders](#other-folders)
  - [License](#license)

## Description

The purpose of this application it to perform web scraping of multiple pages for a website and to also scrape multiple websites.

## Requirements

To use this application, you will need to have Python 3 installed, including pip3.

The application was developed with Python 3.11.6.

## Installation

To install the application, perform the following steps:

1. Open a terminal and change to the directory you would like to download the application to:

    ``` console
    cd <path-to-folder-to-download-to>
    ```

2. Clone the repository to your local system:

    ``` console
    git clone <add-url>
    ```

3. Change to the directory:

    ``` console
    cd multi-site-web-scraper
    ```

4. Create a Python virtual environment:

    ``` console
    python3 -m venv venv
    ```

5. Activate the virtual environment:

    ``` console
    source ./venv/bin/activate
    ```

6. Install the required packages for the application:

    ``` console
    pip3 install -r requirements.txt
    ```

## Usage

Once the application is installed, you will need to define the site(s) you wish to scrape. In the folder named *sites* which contains a zip file called `template.zip`. Unzip this file and rename the folder it creates to that of the site. It is recommended to take the base of the websites URL and use that for the folder name but replace any . with underscores. For example, amazon.co.uk would be amazon_co_uk.

In the folder, there are three files. You can ignore the file called `__init__.py`. The other two files are what needs to be changed.

### pages.xlsx

The pages.xlsx is an Excel spreadsheet that has a number of columns, with the required columns being highlighted in yellow. The purpose of each is:

- url: The URL of the web page.
- browser_to_use: As part of the program, the scraper will send some headers over as part of the request. The headers are determined by the browser listed in this column. The options available are:

  - edge
  - chrome
  - firefox
  - safari

- nickname: This is a short name description that is used in the application for filenames, logging and more. Please use a unique name for each row and use **underscores** (_) rather than spaces. For example, for an iphone 15 in blue with 128GB of storage can be written as iphone_15_blue_128GB.

The `html_id_1` and `html_class_1` columns are used to identify tags that you want to scrape through on that page. You can add others, just give the columns a unique name. The easiest way is to copy + paste the two columns and then update the number at the end by one.

### processor.py

This is where the processing of the scraped data occurs, with the end result being the data you require being saved to a file or perhaps multiple files. There is one function in the file called process_soup which is where the code for processing the sites page(s) needs to go.

There is no processing code in the template as it is up to you how you want to process the scraped data and how to save it.

There are some guidelines and recommended examples in the file which I would suggest having a read through and looking at the *generic_one_table* *processor.py* file for an example of how to layout / implement the file.

### Other Folders

The other folders and file in the application don't need to be changed for the application to work. You can of course do so if you wish but it is not required.

**NOTE**: Two folders that typically are missing (`log` and `output`) will be created when the application runs.

## License

The license type for this program is the MIT license, correct as of the 18th of October 2023.

Please see the *LICENSE* file in the repository for further details.
