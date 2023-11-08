import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt
import json, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class GPTModel:
    def __init__(self, model):
        self.model = model
        openai.api_key = os.environ['OPENAI_API_KEY']

    @retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(2))
    async def get_completion_with_function_call(self, messages, functions, function_call, model = None):
        if model is None:
            model = self.model
        print(model)
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            functions=functions,
            function_call=function_call,
            seed=42,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        result = response.choices[0]['message']['function_call']['arguments']
        return result
    @retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(2))
    async def get_completion(self, messages, model = None):
        if model is None:
            model = self.model
        print(model)
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            seed=42,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        result = response.choices[0]["message"]["content"]
        return result