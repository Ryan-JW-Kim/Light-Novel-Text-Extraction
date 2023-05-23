import os
import json
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
