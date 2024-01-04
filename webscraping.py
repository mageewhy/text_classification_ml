import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import csv


URL = "https://edition.cnn.com/"

URL_scrape = requests.get(URL)

# Check the status code to ensure the request was successful (200 OK)
if URL_scrape.status_code == 200:
    # Parsing the HTML 
    soup = BeautifulSoup(URL_scrape.content, 'html.parser')
    
    # Find all elements containing headlines (you might need to adjust the tag and class)
    news_titles = soup.find_all("span", class_="container__headline-text")
    news_url = soup.find_all("a", class_="container__link container__link--type-article container_lead-plus-headlines-with-images__link container_lead-plus-headlines-with-images__left container_lead-plus-headlines-with-images__light")
    
    # Extracting titles and categories
    headlines_with_categories = []
    
    for title, url in zip(news_titles, news_url):
        news_title = title.text.strip()
        href = url['href']
        
        parsed_url = urlparse(href)
        path_segments = parsed_url.path.split('/')
        
        if 'business' in path_segments:
            category = 'b'
        elif 'tech' in path_segments:
            category = 't'
        elif 'entertainment' in path_segments:
            category = 'e'
        elif 'health' in path_segments:
            category = 'm'
        else:
            category = 'Other'
        
        headlines_with_categories.append((news_title, category))
    
    # Displaying the headlines and their categories
    for title, category in headlines_with_categories:
        print(f"Title: {title} - Category: {category}")
        
    
      
else:
    print("Failed to retrieve the page")
    
