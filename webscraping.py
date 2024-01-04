import requests
from bs4 import BeautifulSoup

req = requests.get("https://edition.cnn.com/world")

print(req)

# Parsing the HTML 
soup = BeautifulSoup(req.content, 'html.parser') 

# Getting the title tag 
print(soup.title) 
  
# Getting the name of the tag 
print(soup.title.name) 
  
# Getting the name of parent tag 
print(soup.title.parent.name) 