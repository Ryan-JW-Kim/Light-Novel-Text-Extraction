import mechanize
from bs4 import BeautifulSoup


def write_text_file(text: list, file_name: str, dir: str) -> None:
    """
    Write a given chapter to its related download folder

    Input:
        text: list of strings, each string is a line in the chapter
        file_name: string, the name of the file to be written
        dir: string, the name of the directory to write the file to

    """
    with open(f"{dir}/{file_name}.txt", "w", encoding="UTF-8") as f:
        for line in text:
            f.write(line + "\n")

def parse_chapter_webpage(requests_result):
    soup = BeautifulSoup(requests_result.text, "html.parser")
    table = soup.find("div", {"id": "chr-content"})
    divs = table.findAll("p")
    text_lines = []
    for elem in divs:
        for row in elem:
            try:
                _ = row.display
            except:
                text = row.text.strip()
                if text != "":
                    text_lines.append(row.text)


    return text_lines

class SiteSpecificScraper:

    def __init__(self, url="https://read-novelfull.com/readnovelfull/reincarnation-of-the-strongest-sword-god#tab-chapters-title"):
        """
        This class is used to scrape urls from a specific website, in this case https://read-novelfull.com/
        
        self.url = url to be scraped form
        self.urls = list of urls related to each chapter of the book
        """

        self.url = url
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