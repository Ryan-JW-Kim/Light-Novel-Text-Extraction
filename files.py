import os
import json
from chatgpt import count_tokens    

class File_Writer:
    @staticmethod
    def write_text_file(text, dir, number):
        
        with open(f"{dir}/{dir}_{number}.txt", "w") as f:
            for line in text:

                try:
                    f.write(line)

                except UnicodeEncodeError:
                    f.write("")
                    print(f"UnicodeEncodeError: {line}")

    @staticmethod
    def create_directory(folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

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
