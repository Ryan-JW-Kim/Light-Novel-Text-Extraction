import openai
from API_SECRETS import API_KEY

openai.api_key = API_KEY

class Model:
    def __init__(self):
        self.model = "text-davinci-003"
        self.temperature = 0.6
        self.max_tokens = 100

    def run(self, prompt):
        return openai.Completion.create(self.model, prompt, self.temperature, self.max_tokens)