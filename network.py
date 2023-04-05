import requests
from bs4 import BeautifulSoup

class Network:
    run = True

    @staticmethod
    def perform_request(url):
        
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(e)
            Network.run = False
            return False
    
    @staticmethod
    def parse_html(html):
        soup = BeautifulSoup(html.text, 'html.parser')
        soup.prettify()

        return soup
    
    @staticmethod
    def extract_text_div(soup):
        
        lines = []

        for seg in soup.find_all("p"):
            lines.append(seg.text)
            lines.append("\n")
        
        return lines