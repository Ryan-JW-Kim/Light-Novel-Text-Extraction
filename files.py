import os

class File_Writer:
    @staticmethod
    def write_text_file(text, dir, number):
        
        with open(f"{dir}/{dir}_{number}.txt", "w") as f:
            f.writelines(text)

    @staticmethod
    def create_directory(folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)