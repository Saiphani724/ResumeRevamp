from pydantic import BaseModel
from resume_gen import parse_resume, parse_job_details, generate_resume, generate_latex_resume
from fastapi.responses import RedirectResponse
# from common.constants import job_details_json, resume_json
from fastapi.responses import HTMLResponse
import time

def register_routes(app):

    class RequestBody(BaseModel):
        resumeTxt: str
        jobDetails: str

    @app.get("/")
    async def index():
        return RedirectResponse(url="/resumerevamp/ui/v1")
    
    @app.get("/resumerevamp/ui/v1")
    async def home():
        with open('frontend/home.html', 'r') as file:
            html_content = file.read()
        return HTMLResponse(content=html_content, status_code=200)

    @app.post(f"/resumerevamp/api/v1")
    async def revamp_resume(body: RequestBody):
        resume = body.resumeTxt
        job_details = body.jobDetails
        
        start_time = time.time()
        resume_json = await parse_resume(resume)
        resume_parsing_end_time = time.time()
        print("Resume Parsed in %f seconds" % (resume_parsing_end_time - start_time))
        job_details_json = await parse_job_details(job_details)
        jd_parsing_end_time = time.time()
        print("Job Details Parsed in %f seconds" % (jd_parsing_end_time - resume_parsing_end_time))
        resume_new = await generate_resume(resume_json, job_details_json)
        resume_gen_end_time = time.time()
        # print(resume_new)
        print("Resume Revamped in %f seconds" % (resume_gen_end_time - jd_parsing_end_time))
        resume_latex = await generate_latex_resume(resume_new)
        latex_gen_end_time = time.time()
        print("Latex Created in %f seconds" % (latex_gen_end_time - resume_gen_end_time))
        print("Total time taken: %f seconds" % (latex_gen_end_time - start_time))
        return {
            "resume_latex": resume_latex
        }