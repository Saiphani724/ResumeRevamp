from pydantic import BaseModel
from resume_gen import parse_resume, parse_job_details, generate_resume, generate_latex_resume
from fastapi.responses import RedirectResponse
from common.constants import job_details_json, resume_json
import time

def register_routes(app):

    class RequestBody(BaseModel):
        resume: str
        job_details: str

    @app.get("/")
    async def index():
        return RedirectResponse(url="/resumerevamp/api/v1")
    
    @app.get("/resumerevamp/api/v1")
    async def home():
        return "Server is up and running!"

    @app.post(f"/resumerevamp/api/v1")
    async def revamp_resume(body: RequestBody):
        resume = body.resume
        job_details = body.job_details
        
        # resume_json = await parse_resume(resume)
        # job_details_json = await parse_job_details(job_details)
        start_time = time.time()
        resume_new = await generate_resume(resume_json, job_details_json)
        print("Resume Generated in %s seconds" % (time.time() - start_time))
        resume_latex = await generate_latex_resume(resume_new)
        return {
            "resume": "latex resume"
        }