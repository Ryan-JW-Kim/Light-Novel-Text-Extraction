from files import *


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

def manual_main():
    
    url = ""

    Network.last_instance = Network.instance(url)

    while Network.unstopped is True:

        url = Network.get_next_url(url)

        File_Writer.write_file(Network.last_instance.data)    
    
    
    File_Writer.mass_tokenize(batches=-1, optimal_size=4096)

    for batch in File_Writer.tokenized_batches:

        print(batch.shape)

        # Pause until user enters any input
        input("")



if __name__ == '__main__':
    manual_main()