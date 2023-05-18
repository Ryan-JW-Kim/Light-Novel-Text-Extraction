import cloudscraper
from datetime import datetime
import threading
from files import *
from network import SiteSpecificScraper
import sys
import requests

sys.path.insert(0, "../Python-Proxy")
from proxy import FreeProxyList, ProxyTools

def testing():
    scraper = Scraper()
    scraper.save_proxies()
    proxies_filename = "scraped_proxies.txt"
    ProxyParser.parse_raw(proxies_filename)

    proxies = []
    for valid in ProxyParser.valid_proxy_generator(proxies_filename):
        proxies.append(valid)
        print(f"Valid: {valid['IP Address']}:{valid['Port']}")

    book_webdata = SiteSpecificScraper()
    batches = book_webdata.divide_batches(proxies, 5)

    threads = []

    for batch in batches:
        batch_obj = ProxyBatch(batch["Proxies"], batch["Book_Urls"], batch["Batch_Number"])
        thread = threading.Thread(target=batch_obj.execute_batch)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    result_list = []
    for batch in batches:
        result_list.append(batch.result)

    directory = f"downloaded_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    File_Writer.create_directory(directory)

    count = 1 
    for result in result_list:
        File_Writer.write_text_file(result["Text"], directory, count)
        count += 1

def testing_new():

    proxy_list = FreeProxyList().proxies_data
    book_webdata = SiteSpecificScraper()    

    scraper = cloudscraper.create_scraper(delay=5, browser="chrome")

    completed = []
    passed = []

    proxy_index = 0
    max_index = len(proxy_list) - 1

    for url in book_webdata.urls:

        proxy = proxy_list[proxy_index]
        while ProxyTools.test_proxy(proxy) is False and proxy["Https"] is False:
            proxy_index += 1
            if proxy_index > max_index:
                print("No more proxies to test")
                sys.exit()
            proxy = proxy_list[proxy_index]

        print(f"Trying proxy: {proxy['IP Address']}:{proxy['Port']}")

        # try:
        response = scraper.get(url, proxies=ProxyTools.format_proxy(proxy))
        print(f"Downloaded: {url}")
        print(response.text)
        completed.append(url)
        break
        # except Exception as e:
        #     break
        #     print(f"Failed to download: {url} with error: {e}")
        #     passed.append(url)


    # folder_name = f"downloaded_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    # os.mkdir(folder_name)


if __name__ == '__main__':
    
    testing_new()