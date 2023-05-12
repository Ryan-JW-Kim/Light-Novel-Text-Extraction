import sys
from files import *
from network import Network, SiteSpecificScraper
from chatgpt import count_tokens
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

    grace_period = 2

    if save_data:
        File_Writer.create_directory(output_name)

    # For each file in output file, if it existed already
    max = 0
    for file in os.listdir(output_name):
        # Split filename 
        num = int(file.split("_")[-1].split(".")[0])

        if num > max:
            max = num

    if max > chapter_number:
        chapter_number = max + 1

    while Network.run is True and chapter_number <= stop_at:

        time.sleep(grace_period)
        
        curr_url = ''.join(url) % chapter_number

        print("Current URL: %s" % curr_url)

        html = Network.perform_request(curr_url)
        
    
        if html:
            data = Network.parse_html(html)        
            text = Network.extract_text_div(data)

            if save_data is True:
                File_Writer.write_text_file(text, output_name, chapter_number)
            
            print(f"Completed: {curr_url}\n")
            chapter_number += 1

def manual_output():

    context_window = 32000
    token_map = write_token_legend("shadow_slave")

    # -----------------------------------
    # ---- Manage Token Optimization ----
    # -----------------------------------

        # -----------------------------------
        # -- Generate token map for files ---
        # -----------------------------------

        # -----------------------------------
        # -- Create ranges for easy access --
        # -----------------------------------

    # -----------------------------------
    # ---- Manage Displaying Output ----
    # -----------------------------------

        # -----------------------------------
        # -------- For each Range -----------
        # -----------------------------------

            # -----------------------------------
            # -For each chapter as per token map-
            # -----------------------------------


                # -----------------------------------
                # ----- Add to context window -------
                # -----------------------------------


        # -----------------------------------
        # ----Create per chapter prompt -----
        # -----------------------------------


        # -----------------------------------
        # ---Deliver prompt to fine tuned ---
        # -----------------------------------


        # -----------------------------------
        # ------ Process response into ------
        # ------ descriptive parcel ---------
        # -----------------------------------


        # -----------------------------------                    fine tuned 2 is a specific model for taking descriptive parcels from
        # --Feed parcel into fine tuned 2---                     fine tuned and generating a prompt for image ai
        # -----------------------------------


if __name__ == '__main__':
    # manual_extract()
    # manual_output()
    SiteSpecificScraper()