from pydantic import BaseModel
from resume_gen import parse_resume, parse_job_details, generate_resume, generate_latex_resume
from fastapi.responses import RedirectResponse
from common.constants import job_details_json, resume_json
import time

def register_routes(app):

    class RequestBody(BaseModel):
        resumeTxt: str
        jobDetails: str

    @app.get("/")
    async def index():
        return RedirectResponse(url="/resumerevamp/api/v1")
    
    @app.get("/resumerevamp/api/v1")
    async def home():
        return "Server is up and running!"

    @app.post(f"/resumerevamp/api/v1")
    async def revamp_resume(body: RequestBody):
        resume = body.resumeTxt
        job_details = body.jobDetails
        
        # resume_json = await parse_resume(resume)
        # job_details_json = await parse_job_details(job_details)
        start_time = time.time()
        resume_new = await generate_resume(resume_json, job_details_json)
        resume_gen_end_time = time.time()
        print(resume_new)
        print("Resume Generated in %f seconds" % (resume_gen_end_time - start_time))
        time.sleep(10)
        resume_latex = await generate_latex_resume(resume_new)
        latex_gen_end_time = time.time()
        print("Resume Generated in %f seconds" % (latex_gen_end_time - resume_gen_end_time))
        return {
            "resume_latex": resume_latex
        }