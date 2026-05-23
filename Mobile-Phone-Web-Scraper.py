# Install required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime as dt
from tqdm import tqdm

main_url = "https://unique.com.mm/collections/mobile-phone"
########### Part1 - Create URLs ###########
def create_urls(web_url):
    """Create urls from the main url."""
    # Step1 - Request data from the website
    ## Get data by using url
    response = requests.get(web_url)
    ## Extract html, css, etc.
    web_data = response.text

    # Step2 - Create a beautifulsoup object to read web data
    bsObj = BeautifulSoup(web_data, "html5lib")

    # Step3 - Extract Last Page Number
    last_page_tag_list = bsObj.find_all("a", "pagination__nav-item link")
    last_page_tag = last_page_tag_list[-1]
    last_page_text = int(last_page_tag.text)

    # Step4 - Create urls for other web pages
    created_url_list = []
    created_url_list.append(web_url)
    for num in range(2, last_page_text+1):
        new_url = web_url + "?page=" + str(num)
        created_url_list.append(new_url)
    print("URL links are created successfully!")
    return created_url_list

def get_product_info_tags(url):
    """Extract Product Info Tags and return as a list."""
    # Step1 - Request data from the website
    ## Get data by using url
    response = requests.get(url)

    ## Extract html, css, etc.
    web_data = response.text

    # Step2 - Create a beautifulsoup object to read web data
    bsObj = BeautifulSoup(web_data, "html5lib")

    # Step3 - Extract and insert data into the lists
    ## Extract all product info main tags
    product_info_tags_list = bsObj.find_all("div", "product-item__info-inner")
    return product_info_tags_list

def create_name_list(product_info_tags_list):
    """Extract product name from the product info tag, and create a product name list."""
    name_list = []
    for product_info_tag in product_info_tags_list:

        ## Extract product name tag
        product_name_tag = product_info_tag.find("a", "product-item__title text--strong link")
        ## Extract product name
        product_name = product_name_tag.text
        name_list.append(product_name)
    return name_list

def create_price_list(product_info_tags_list):
    """ Extract product price form the product info tag, and create a product price list."""
    price_list = []
    for product_info_tag in product_info_tags_list:
        ## Extract product price tag
        product_price_tag = product_info_tag.find("div", "product-item__price-list price-list")
        ## Extract product price
        product_price = product_price_tag.text
        ## Transform product price
        product_price = product_price.replace(",", "")
        product_price = product_price.replace("K", "")
        product_price = product_price.replace("From", "")
        try:
            product_price = int(product_price) 
            price_list.append(product_price)
        except ValueError:
            # Handle the discount prices
            discount_price_list = product_price.split("\n")
            # get last value
            product_price = discount_price_list[-1]
            # remove spaces from the text
            product_price = product_price.strip()
            product_price = int(product_price) 
            price_list.append(product_price)
    return price_list

def create_status_list(product_info_tags_list):
    """ Extract product status form the product info tag, and create a product status list."""
    status_list = []
    for product_info_tag in product_info_tags_list:
        ## Extract product status tag
        status_class_list = ["product-item__inventory inventory", "product-item__inventory inventory inventory--high", "product-item__inventory inventory inventory--low"]
        for status_class in status_class_list:
            result = product_info_tag.find("span", status_class)
            if result != None:
                product_status_tag = result
                product_status = product_status_tag.text
                status_list.append(product_status)
    return status_list


def get_current_dt():
    """Create current date&time string."""
    # Get current date&time
    current_datetime = dt.now()
    current_datetime = str(current_datetime).replace(":", "-").split(".")[0]
    return current_datetime

#################### Main Program ####################

def main():
    """Main program to extract data from the website."""
    # Step1 - Create urls for all web pages
    url_list = create_urls(main_url)

    # Step2 - Extract data from each url of the url list
    url_count = 0
    final_df = pd.DataFrame() #create an empty dataframe
    for each_url in tqdm(url_list):
        ## Extract product info tags
        p_info_tags_list = get_product_info_tags(each_url)

        ## Create product name list
        p_name_list = create_name_list(p_info_tags_list)
        
        ## Create product price list
        p_price_list = create_price_list(p_info_tags_list)
        
        ## Create product status list
        p_status_list = create_status_list(p_info_tags_list)
        
        ## Create page level dataframe
        page_df = pd.DataFrame({"Product Name":p_name_list,
                           "Price":p_price_list,
                           "Status":p_status_list})
        
        ## Get current datetime as string
        current_dt = get_current_dt()
        
        url_count += 1
        # Export as page level excel file
        page_df.to_excel(f"Output_{url_count}_{current_dt}.xlsx", index = False)
        print(f"Web Page {url_count} is successfully completed!")
        
        # Export data from all web pages.
        final_df = pd.concat([final_df, page_df])

    # Export the final dataframe as an excel file.
    final_df.to_excel(f"All Data_{current_dt}.xlsx", index = False)

    print("The Project is completed successfully!")

if __name__ == "__main__":
    main()
    

