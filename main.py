import cloudscraper
from datetime import datetime
import threading
from files import *
from network import SiteSpecificScraper
import sys
import requests

sys.path.insert(0, "../Python-Proxy")
from proxy import FreeProxyList, ProxyTools

def testing_new():

    proxy_list = FreeProxyList().proxies_data
    book_webdata = SiteSpecificScraper()    

    folder_name = f"downloaded_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    os.mkdir(folder_name)

    scraper = cloudscraper.create_scraper(delay=5, browser="chrome")

    completed = []
    passed = []

    proxy_index = 0
    max_index = len(proxy_list) - 1
    
    chapter_count = 1

    for url in book_webdata.urls:

        proxy = proxy_list[proxy_index]
        proxy_index += 1

        print(f"Trying proxy: {proxy['IP Address']}:{proxy['Port']}")

        try:
            response = scraper.get(url, proxies=ProxyTools.format_proxy(proxy))
            print(f"Downloaded: {url}")
            text = File_Writer.parse_chapter_webpage(response)
            File_Writer.write_text_file(text, folder_name, chapter_count)
            completed.append(url)
            chapter_count += 1
            
        except Exception as e:
            print(f"Failed to download: {url} with error: {e}")
            passed.append(url)
    
        break

if __name__ == '__main__':
    
    testing_new()