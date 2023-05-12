from datetime import datetime
import threading
from files import *
from network import SiteSpecificScraper
import sys
sys.path.insert(0, "../Python-Proxy")
from proxy import ProxyParser, ProxyBatch
from proxy_list_scraper import Scraper

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

if __name__ == '__main__':
    
    testing()