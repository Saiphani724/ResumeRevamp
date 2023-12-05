from common.parser_helpers import get_job_details_messages, get_parse_resume_messages
from common.resume_gen_helpers import get_resume_gen_messages
from common.latex_resume_gen_helper import get_resume_latex_gen_messages
from gpt_model import GPTModel, GPTAssistantModel
import json

model_gpt35 = GPTModel("gpt-3.5-turbo-0613")
# model_gpt4 = GPTModel("gpt-4-0613")
model_gpt4 = GPTModel("gpt-4-1106-preview")

model = GPTAssistantModel()

async def parse_resume(resume):
    messages = get_parse_resume_messages(resume)
    resume_json = await model_gpt35.get_completion(messages)
    return resume_json

async def parse_job_details(job_details):
    messages = get_job_details_messages(job_details)
    job_details_json = await model_gpt35.get_completion(messages)
    return job_details_json

# async def generate_resume(resume_json, job_details_json):
#     resume_new = {}
#     messages = get_resume_gen_messages(resume_json, job_details_json)
#     functions = resume_gen_functions
#     function_call = {"name": "revamp_resume"}
#     resume_new = await model_gpt4.get_completion_with_function_call(
#         messages, functions, function_call
#     )
#     return resume_new


def generate_latex_resume(resume_json, job_details_json, comments, thread_id):
    if thread_id == "":
        messages = get_resume_gen_messages(resume_json, job_details_json, comments)
    else:
        messages = [{
            "role": "user",
            "content": comments,
        }]
    print(messages)
    resume_latex, thread_id = model.get_completion(messages, thread_id)
    return resume_latex, thread_id
