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
    
class SiteSpecificScraper:

    def __init__(self):
        """
        This class is used to scrape a specific website and will not work otherwise.

        url: https://read-novelfull.com/readnovelfull/reincarnation-of-the-strongest-sword-god#tab-chapters-title

        In which the novel information for the title "Reincarnation Of The Strongest Sword God" is stored
        """

        # self.url = "https://read-novelfull.com/readnovelfull/reincarnation-of-the-strongest-sword-god#tab-chapters-title"
        self.test_file = "downloaded_test_page.html"

        # self.html = requests.get(self.url)
        with open(self.test_file, "r", encoding="UTF-8") as f:
            content = f.read()
            
            self.soup = BeautifulSoup(content, 'html.parser')

        panel = self.soup.find("div", {"class": "panel-body"})
        rows = panel.findAll("li")

        urls = []

        for row in rows:
            segments = row.find("a").prettify().split(" ")
            for segment in segments:
                if "href=" in segment:
                    segment = segment.replace("href=", "")
                    while "\"" in segment:
                        segment = segment.replace("\"", "")
                    
                    urls.append(segment)
            
        for url in urls:
            print(url)
            
