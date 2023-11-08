from common.parser_helpers import get_parse_resume_prompt, get_job_details_prompt
from common.resume_gen_helpers import get_resume_gen_messages, resume_gen_functions
from gpt_model import GPTModel
import json

model = GPTModel("gpt-4-1106-preview")


async def parse_resume(resume):
    resume_json = {}
    return resume_json


async def parse_job_details(job_details):
    job_details_json = {}
    return job_details_json


async def generate_resume(resume_json, job_details_json):
    resume_new = {}
    messages = get_resume_gen_messages(resume_json, job_details_json)
    functions = resume_gen_functions
    function_call = {"name": "revamp_resume"}
    resume_new = await model.get_completion_with_function_call(
        messages, functions, function_call
    )
    print(resume_new)
    return resume_new


async def generate_latex_resume(resume_new):
    resume_latex = json.dumps(resume_new)
    return resume_latex
