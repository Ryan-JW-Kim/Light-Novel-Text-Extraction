import mechanize
import requests
from bs4 import BeautifulSoup
    
class SiteSpecificScraper:

    def __init__(self):
        """
        This class is used to scrape a specific website and will not work otherwise.

        url: https://read-novelfull.com/readnovelfull/reincarnation-of-the-strongest-sword-god#tab-chapters-title

        In which the novel information for the title "Reincarnation Of The Strongest Sword God" is stored

        """

        self.url = "https://read-novelfull.com/readnovelfull/reincarnation-of-the-strongest-sword-god#tab-chapters-title"
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        resp = br.open(self.url)

        self.soup = BeautifulSoup(resp.read(), "html.parser")

        panel = self.soup.find("div", {"class": "panel-body"})
        rows = panel.findAll("li")

        self.urls = []

        for row in rows:
            segments = row.find("a").prettify().split(" ")
            for segment in segments:
                if "href=" in segment:
                    segment = segment.replace("href=", "")
                    while "\"" in segment:
                        segment = segment.replace("\"", "")
                    
                    self.urls.append(segment)