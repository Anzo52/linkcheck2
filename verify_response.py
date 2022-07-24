import requests
from bs4 import BeautifulSoup

url = input("Enter a URL: ")

page = requests.get(url)
response_code = str(page.status_code)
data = page.text
soup_text = BeautifulSoup(data)

for link in soup_text.find_all('a'):
    print(f"URL: {link.get('href')}" + f"| Status Code: {response_code}")
