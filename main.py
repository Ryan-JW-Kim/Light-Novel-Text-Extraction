import cloudscraper
from datetime import datetime
from tools import *
import os
import sys
import time

# Import the proxy module from https://github.com/Ryan-JW-Kim/Python-Proxy
sys.path.insert(0, "../Python-Proxy")
from proxy import FreeProxyList, ProxyTools

def Download_Book(user_input=None):

    # Download a list of free proxies from proxy module
    proxy_list = FreeProxyList().proxies_data

    # Scrape list of chapter from https://read-novelfull.com/
    if user_input is None:
        book_webdata = SiteSpecificScraper()    

    else:
        try:
            book_webdata = SiteSpecificScraper(user_input)

        except Exception as e:
            print(f"Failed to collect with error: {e}\n\t- Using url {user_input}")
            return

    # Make a folder with the current date and time
    folder_name = f"downloaded_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    os.mkdir(folder_name)

    # Create a cloudscraper object to bypass cloudflare
    scraper = cloudscraper.create_scraper(delay=5, browser="chrome")

    completed = []
    passed = []

    proxy_index = 0
    max_proxy_index = len(proxy_list) - 1
    
    for url in book_webdata.urls:
        
        if proxy_index > max_proxy_index:
            proxy_index = 0
            
        proxy = proxy_list[proxy_index]
        proxy_index += 1

        print(f"\nTrying proxy: {proxy['IP Address']}:{proxy['Port']}")

        # Wait 1 second, as to not spam the website with requests (unless website is sufficently fast, and you dont mind Ddos-ing it)
        time.sleep(3) 

        try:
            response = scraper.get(url, proxies=ProxyTools.format_proxy(proxy))
            text = parse_chapter_webpage(response)
            file_name = url.split("/")[-1]
            write_text_file(text, file_name, folder_name)
            print(f"    Downloaded: {url}")
            completed.append(url)
            
        except Exception as e:
            print(f"    Failed to download: {url} with error: {e}")
            passed.append(url)
    
    print(f"Completed: {len(completed)}")
    print(f"Failed: {len(passed)}")

if __name__ == '__main__':
    
    user_inpt = input("Enter url: ")

    if user_inpt == "":
        Download_Book()
    elif "https://read-novelfull.com/" in user_inpt:
        Download_Book(user_inpt)

    else:
        print("Invalid url")