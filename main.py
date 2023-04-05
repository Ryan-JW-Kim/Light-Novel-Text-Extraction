from files import *
from network import Network
import time

def main():

    url = ""
    target_individual = ["Sunny"]

    # Describe to model how image ai should be instructed

    # Complile files into text files

    # For each file

        # Generate response for describing the target individual

        # Save list of descriptions into file.

    
    # Prompt model into recieving descriptions of target individual

    # For description:
        
        # Present description

    # Request prompt for image ai given the descriptions

    # Save prompt output

    pass

def manual_extract():
    
    url = "https://webnovelfull.net/read-novel/shadow-slave/chapter-%s"
    output_name = "shadow_slave"
    chapter_number = 1
    stop_at = 50
    save_data = True

    if save_data:
        File_Writer.create_directory(output_name)

    while Network.run is True and chapter_number <= stop_at:
        curr_url = ''.join(url) % chapter_number

        print("Current URL: %s" % curr_url)

        html = Network.perform_request(curr_url)
        
    
        if html:
            data = Network.parse_html(html)        
            text = Network.extract_text_div(data)

            if save_data is True:
                File_Writer.write_text_file(text, output_name, chapter_number)
            
            print(f"Completed: {curr_url}")
            chapter_number += 1

def manual_output():
    pass

if __name__ == '__main__':
    # manual_extract()
    manual_output()