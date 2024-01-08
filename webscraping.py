import csv
import time
import os
import webscraping
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Open the websites
news_url = webscraping.URLs()

def scrape_cnn_data(url):
    driver.get(url)
    total_pages = 15
    
    all_cnn_data = []
    
    for page in range(1, total_pages + 1):
        print(f"Scraping Page {page}")
        
        titles = driver.find_elements(By.XPATH, "//span[@class='container__headline-text']")
        category = parse_qs(urlparse(url).query)['q'][0]

        if category.lower() == 'business':
            category = 'b'
        elif category.lower() == 'entertainment':
            category = 'e'
        elif category.lower() == 'technology':
            category = 't'
        elif category.lower() == 'science':
            category = 't'
        elif category.lower() == 'health':
            category = 'm'
        
        scraped_data = []
        for title in titles:
            scraped_data.append({
                'TITLE': title.text,
                'CATEGORY': category
            })
        
        all_cnn_data.extend(scraped_data)

        # Navigate to next page
        try:
            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='pagination-arrow pagination-arrow-right search__pagination-link']/span[@class='pagination-arrow-text']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            next_button.click()

            time.sleep(3)
        except Exception as e:
            print(f"Error: {e}")
            break  # Break the loop if unable to find the next button
    
    return all_cnn_data
    
def scrape_bbc_data(url):
    driver.get(url)
    total_pages = 5
    
    all_bbc_data = []
    
    for page in range(1, total_pages + 1):
        print(f"Scraping Page {page}")
        
        titles = driver.find_elements(By.XPATH, "//p[@class='ssrcss-6arcww-PromoHeadline']")
        category = parse_qs(urlparse(url).query)['q'][0]

        if category.lower() == 'business':
            category = 'b'
        elif category.lower() == 'entertainment':
            category = 'e'
        elif category.lower() == 'technology':
            category = 't'
        elif category.lower() == 'science':
            category = 't'
        elif category.lower() == 'health':
            category = 'm'
        
        scraped_data = []
        for title in titles:
            scraped_data.append({
                'TITLE': title.text,
                'CATEGORY': category
            })
        
        all_bbc_data.extend(scraped_data)

        # Navigate to next page
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ssrcss-3vkeha-StyledButtonContent']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()

        time.sleep(3)
    
    return all_bbc_data

def scrape_apnews_data(url):
    driver.get(url)
    total_pages = 50
    
    all_apnews_data = []
    
    for page in range(1, total_pages + 1):
        print(f"Scraping Page {page}")
        
        titles = driver.find_elements(By.XPATH, "//span[@class='PagePromoContentIcons-text']")
        category = parse_qs(urlparse(url).query)['q'][0]

        if category.lower() == 'business':
            category = 'b'
        elif category.lower() == 'entertainment':
            category = 'e'
        elif category.lower() == 'technology':
            category = 't'
        elif category.lower() == 'science':
            category = 't'
        elif category.lower() == 'health':
            category = 'm'
        
        scraped_data = []
        for title in titles:
            scraped_data.append({
                'TITLE': title.text,
                'CATEGORY': category
            })
        
        all_apnews_data.extend(scraped_data)

        # Navigate to next page
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='Pagination-nextPage']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()

        time.sleep(3)
    
    return all_apnews_data
   
def scrape_abcnews_data(url):
    driver.get(url)
    total_pages = 100
    
    all_abcnews_data = []

    for page in range(1, total_pages + 1):
        print(f"Scraping Page {page}")
        
        titles = driver.find_elements(By.XPATH, "//div[@class='ContentRoll__Headline']/h2/a[@class='AnchorLink']")
        category = parse_qs(urlparse(url).query)['q'][0]

        if category.lower() == 'business':
            category = 'b'
        elif category.lower() == 'entertainment':
            category = 'e'
        elif category.lower() == 'technology':
            category = 't'
        elif category.lower() in ['science', 'health']:
            category = 'm'
        
        scraped_data = []
        for title in titles:
            scraped_data.append({
                'TITLE': title.text,
                'CATEGORY': category
            })
        
        all_abcnews_data.extend(scraped_data)

        # Navigate to the next page using the provided XPath for the "Next" button
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='fitt-analytics']/div/main/div[2]/section[1]/div/div[4]/a[2]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()

        time.sleep(3)

    return all_abcnews_data

def generate_search_url(news_source, query):
    base_url = ""
    params = {}

    if news_source.lower() == 'cnn':
        base_url = "https://edition.cnn.com/search"
        params = {
            'q': query,
            'from': '0',
            'size': '50',
            'page': '1',
            'sort': 'newest',
            'types': 'all',
            'section': '',
        }
    elif news_source.lower() == 'bbc':
        base_url = "https://www.bbc.co.uk/search"
        params = {
            'q': query,
            'seqId': '63f76c50-ad81-11ee-93be-177d84e088a8',
            'd': 'HOMEPAGE_GNL'
        }
    elif news_source.lower() == 'apnews':
        base_url = "https://apnews.com/search"
        params = {
            'q': query,
            'nt': 'navsearch'
        }
    elif news_source.lower() == 'abcnews':
        base_url = "https://abcnews.go.com/search"
        params = {
            'searchtext': query
        }
    else:
        return None  # Return None for unsupported news sources

    # Constructing the URL with parameters
    search_url = f"{base_url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
    return search_url

def URLs():
    news_sources = ["CNN", "BBC", "APNEWS", "ABCNEWS"]
    news_queries = ["Business", "Entertainment", "Technology", "Science", "Health"]
    all_urls = []
    
    # Generating search URLs for different news sources
    for news_source in news_sources:
        for news_query in news_queries:
            url = generate_search_url(news_source, news_query)
            if url:  # Check if a valid URL is generated
                all_urls.append(url)
    
    return all_urls


def save_to_csv(news_data, file_name):
    with open(file_name, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["TITLE", "CATEGORY"])
        for data in news_data:
            writer.writerow([data['TITLE'], data['CATEGORY']])

def scrape_data(urls):
    all_news_data = {}  # Initialize a dictionary to store data by news source

    for url in urls:
        scraped_data = []  # Initialize scraped_data within the loop
        if "cnn.com" in url:
            scraped_data = scrape_cnn_data(url)
            all_news_data['cnn'] = scraped_data  # Store scraped data for CNN
        elif "bbc.com" in url:
            scraped_data = scrape_bbc_data(url)
            all_news_data['bbc'] = scraped_data  # Store scraped data for BBC
        elif "apnews.com" in url:
            scraped_data = scrape_apnews_data(url)
            all_news_data['apnews'] = scraped_data  # Store scraped data for AP News
        elif "abcnews.go" in url:
            scraped_data = scrape_abcnews_data(url)
            all_news_data['abcnews'] = scraped_data  # Store scraped data for ABC News
        else:
            scraped_data = []  # Handle other websites
            print(f"Unsupported URL: {url}")

    # Save each news source's data to a separate CSV file
    for source, data in all_news_data.items():
        if data:
            csv_file = f"webscrape_data/{source}_news.csv"
            save_to_csv(data, csv_file)
            print(f"Data for {source.upper()} saved to '{csv_file}'")
        else:
            print(f"No data scraped for {source.upper()}")

# Scrape the data
scrape_data(news_url)
