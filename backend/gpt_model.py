import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt
import json

class GPTModel:
    def __init__(self, model):
        self.model = model
        openai.api_key = 'OPENAI_API_KEY'

    @retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(2))
    async def get_completion_with_function_call(self, messages, functions, function_call, model = None):
        if model is None:
            model = self.model
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            functions=functions,
            function_call=function_call,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        result = response.choices[0]['message']['function_call']['arguments']
        return result