import requests
from bs4 import BeautifulSoup
import csv
import urls_list

def clean_text(text):
    clean_text = text.encode('latin1', 'ignore').decode('utf-8', 'ignore')
    return clean_text

def scrape_cnn_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []

    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')
        news_titles = soup.find_all("span", class_="container__headline-text")
        news_links = soup.find_all("a", class_="container__link")

        for title, link in zip(news_titles, news_links):
            news_title = clean_text(title.text.strip())
            href = link['href']
            
            if 'business' in href:
                category = 'b'
            elif 'tech' in href:
                category = 't'
            elif any(keyword in href for keyword in ['entertainment', 'sport', 'movie']):
                category = 'e'
            elif any(keyword in href for keyword in ['health', 'wellness']):
                category = 'm'
            else:
                category = 'other'

            try:
                if category == 'other':
                    continue
                headlines_with_categories.append((news_title, category))
            except ValueError as e:
                return e
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list

def scrape_bbc_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []

    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')
        news_titles = soup.find_all("a", class_="media__link")
        news_links = soup.find_all("a", class_="media__link")

        for title, link in zip(news_titles, news_links):
            news_title = clean_text(title.text.strip())
            href = link['href']
            
            if 'business' in href:
                category = 'b'
            elif 'tech' in href:
                category = 't'
            elif any(keyword in href for keyword in ['entertainment', 'sport', 'movie']):
                category = 'e'
            elif any(keyword in href for keyword in ['health', 'wellness']):
                category = 'm'
            else:
                category = 'other'
                
            try:
                if category == 'other':
                    continue
                headlines_with_categories.append((news_title, category))
            except ValueError as e:
                return e
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list

def scrape_ap_entertainment_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []
    category = 'e'

    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')

        # Scrape titles from h3 tags
        h3_titles = soup.find_all("h3", class_="PagePromo-title")
        for h3_title in h3_titles:
            span_title = h3_title.find("span", class_="PagePromoContentIcons-text")
            if span_title:
                news_title = clean_text(span_title.text.strip())
                headlines_with_categories.append((news_title, category))

        # Scrape titles from span tags
        span_titles = soup.find_all("span", class_="video-label video-title")
        for span_title in span_titles:
            news_title = clean_text(span_title.text.strip())
            headlines_with_categories.append((news_title, category))
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list
    
def scrape_ap_business_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []
    category = 'b'
    
    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')

        # Scrape titles from h3 tags
        h3_titles = soup.find_all("h3", class_="PagePromo-title")
        for h3_title in h3_titles:
            span_title = h3_title.find("span", class_="PagePromoContentIcons-text")
            if span_title:
                news_title = clean_text(span_title.text.strip())
                headlines_with_categories.append((news_title, category))

        # Scrape titles from span tags
        span_titles = soup.find_all("span", class_="video-label video-title")
        for span_title in span_titles:
            news_title = clean_text(span_title.text.strip())
            headlines_with_categories.append((news_title, category))
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list

def scrape_ap_tech_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []
    category = 't'

    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')

        # Scrape titles from h3 tags
        h3_titles = soup.find_all("h3", class_="PagePromo-title")
        for h3_title in h3_titles:
            span_title = h3_title.find("span", class_="PagePromoContentIcons-text")
            if span_title:
                news_title = clean_text(span_title.text.strip())
                headlines_with_categories.append((news_title, category))

        # Scrape titles from span tags
        span_titles = soup.find_all("span", class_="video-label video-title")
        for span_title in span_titles:
            news_title = clean_text(span_title.text.strip())
            headlines_with_categories.append((news_title, category))
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list
    
def scrape_ap_health_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []
    category = 'm'
    
    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')

        # Scrape titles from h3 tags
        h3_titles = soup.find_all("h3", class_="PagePromo-title")
        for h3_title in h3_titles:
            span_title = h3_title.find("span", class_="PagePromoContentIcons-text")
            if span_title:
                news_title = clean_text(span_title.text.strip())
                headlines_with_categories.append((news_title, category))

        # Scrape titles from span tags
        span_titles = soup.find_all("span", class_="video-label video-title")
        for span_title in span_titles:
            news_title = clean_text(span_title.text.strip())
            headlines_with_categories.append((news_title, category))
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list

def scrape_nbc_health_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []
    category = 'm'
    
    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')

        h2_titles = soup.find_all("h2", class_="wide-tease-item__headline")
        for title in h2_titles:
            news_title = clean_text(title.text.strip())
            headlines_with_categories.append((news_title, category))
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list

def scrape_nbc_tech_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []
    category = 't'
    
    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')

        h2_titles = soup.find_all("h2", class_="wide-tease-item__headline")
        for title in h2_titles:
            news_title = clean_text(title.text.strip())
            headlines_with_categories.append((news_title, category))
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list

def scrape_nbc_science_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []
    category = 't'
    
    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')

        h2_titles = soup.find_all("h2", class_="wide-tease-item__headline")
        for title in h2_titles:
            news_title = clean_text(title.text.strip())
            headlines_with_categories.append((news_title, category))
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list
    
def scrape_nbc_business_data(url):
    URL_scrape = requests.get(url)
    headlines_with_categories = []
    category = 'b'
    
    if URL_scrape.status_code == 200:
        soup = BeautifulSoup(URL_scrape.content, 'html.parser')

        h2_titles = soup.find_all("h2", class_="wide-tease-item__headline")
        for title in h2_titles:
            news_title = clean_text(title.text.strip())
            headlines_with_categories.append((news_title, category))
            
        return headlines_with_categories # return populated data
    else:
        print(f"Failed to retrieve the page: {url}")
        return headlines_with_categories # return empty list

def scrape_data(urls):
    all_news_data = []  # Initialize a new list for each scrape operation

    for url in urls:
        scraped_data = []  # Initialize scraped_data within the loop
        if "cnn" in url:
            scraped_data = scrape_cnn_data(url)
        elif "bbc" in url:
            scraped_data = scrape_bbc_data(url)
        elif "apnews.com/entertainment" in url:
            scraped_data = scrape_ap_entertainment_data(url)
        elif "apnews.com/business" in url:
            scraped_data = scrape_ap_business_data(url)
        elif "apnews.com/technology" in url:
            scraped_data = scrape_ap_tech_data(url)
        elif "apnews.com/health" in url:
            scraped_data = scrape_ap_health_data(url)
        elif "nbcnews.com/science" in url:
            scraped_data = scrape_nbc_science_data(url)
        elif "nbcnews.com/health" in url:
            scraped_data = scrape_nbc_health_data(url)
        elif "nbcnews.com/business" in url:
            scraped_data = scrape_nbc_business_data(url)
        elif "nbcnews.com/tech-media" in url:
            scraped_data = scrape_nbc_tech_data(url)
        else:
            scraped_data = []  # Handle other websites
            
        all_news_data.extend(scraped_data)

    return all_news_data

# Write all scraped data to a single CSV file
all_data = scrape_data(urls_list.URLs)  # Get the scraped data

with open("webscrape_data/all_news.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["TITLE", "CATEGORY"])
    for data in all_data:
        writer.writerow([clean_text(data[0]), data[1]])  # Clean title before writing to CSV






















# # Get Scraped Data
# test_dataset = scrape_data(urls_list.URLs)

# def save_to_csv(data, filename):
#     with open(filename, "w", newline='', encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["TITLE", "CATEGORY"])
#         writer.writerows(data)
        
# # Save the scraped data to a CSV file
# save_to_csv(test_dataset, "webscrape_data/all_news.csv")
