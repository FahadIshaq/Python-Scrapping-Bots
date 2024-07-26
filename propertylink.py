import requests
from requests import Session

session = Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
})

def fetch_data(url):
    # Initial request to capture cookies
    initial = session.get('https://pladmin.estatesgazette.com')  
    response = session.get(url)  # Subsequent requests will use cookies from the initial
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page: Status Code {response.status_code}")
        return None
