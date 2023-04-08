
import openai
from API_SECRETS import API_KEY

openai.api_key = API_KEY

def count_tokens(data):
    if isinstance(data, str):  # If input is a string
        tokens = data.split()  # Split string into tokens
        return len(tokens)  # Return the number of tokens
    elif isinstance(data, list):  # If input is a list of strings
        tokens = []  # Create an empty list for tokens
        for item in data:  # Iterate over each string in the list
            tokens += item.split()  # Split each string into tokens and add them to the list
        return len(tokens)  # Return the number of tokens
    else:
        raise TypeError("Input must be a string or a list of strings")

class Model:
    def __init__(self):
        self.model = "text-davinci-003"
        self.temperature = 0.6
        self.max_tokens = 100

    def run(self, prompt):
        return openai.Completion.create(self.model, prompt, self.temperature, self.max_tokens)