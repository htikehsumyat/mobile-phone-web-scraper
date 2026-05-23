# Mobile Phone Web Scraper
This project is a **Python-based web scraper** that extracts mobile phone product data from the Unique Myanmar e-commerce website using BeautifulSoup and Pandas. 
The scraper automatically: 
- navigates through all available product pages
- collects product names, prices, and inventory status
- cleans the extracted data, and
- exports the results into timestamped Excel files for further analysis.

## Features
- Automated multi-page web scraping
- Mobile phone product data extraction
- Price cleaning and processing
- Excel export for structured data analysis
- Modular function-based Python design
  
## Technologies & Libraries Used
- Python3 — Core programming language
- requests — Handling HTTP requests
- BeautifulSoup4(bs4) — HTML parsing and web scraping
- pandas — Data processing and Excel export
- tqdm — Progress tracking for scraping operations
- datetime — Generating timestamped output files
- html5lib — HTML parser used by BeautifulSoup

## Installation
1. Clone the repository: git clone https://github.com/your-username/mobile-phone-web-scraper.git
Navigate to the project folder: cd mobile-phone-web-scraper

2. Install required libraries: pip install -r requirements.txt

## How to Run
Run the Python script:

python mobile_phone_web_scraper.py

## Output
The scraper generates:
- Individual Excel files for each page
- A final combined Excel file containing all scraped data

## Learning Outcomes
Through this project, I gained hands-on experience in web scraping using Python, including extracting and processing structured data from an e-commerce website. 
I also strengthened my skills in data cleaning, working with Pandas, and organizing code into modular and reusable functions.

## Disclaimer
- This project is created for **educational and portfolio purposes** only.
- The scraper is intended to demonstrate web scraping techniques and data extraction using Python.
- Website structures may change over time, which may affect or break the functionality of the script.
- Users should ensure compliance with the target website’s terms of service and robots.txt guidelines before running any scraping activity.
- This tool should be used responsibly, avoiding excessive requests that may place unnecessary load on the server.

## Author
Developed by **Htike Hsu Myat**
