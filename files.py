import os
import json
from chatgpt import count_tokens    
from bs4 import BeautifulSoup

class File_Writer:
    @staticmethod
    def write_text_file(text, file_name, dir):
        
        with open(f"{dir}/{file_name}.txt", "w", encoding="UTF-8") as f:
            for line in text:
                f.write(line + "\n")

    @staticmethod
    def parse_chapter_webpage(requests_result):
        soup = BeautifulSoup(requests_result.text, "html.parser")
        table = soup.find("div", {"id": "chr-content"})
        divs = table.findAll("p")

        text_lines = []
        for elem in divs:
            for row in elem:

                try:
                    _ = row.display
                    text_lines.append(row.text)
                
                except:
                    break
    
        return text_lines

def write_token_legend(target_folder: str, output_to_file=False):

    tokens_data =  {}

    # For each file in target
    for file in os.listdir(target_folder):

        # Add token count to tokens_data
        with open(f"{target_folder}/{file}", "r") as f:
            text = f.read()
            tokens_data[file] = count_tokens(text)

    
    # If requested to add to json file
    if output_to_file:
        with open("token_legend.json", "w") as f:
            json.dump(tokens_data, f)
    
    return tokens_data
