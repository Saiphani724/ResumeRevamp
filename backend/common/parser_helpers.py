def get_parse_resume_messages(resume_txt):
    prompt = f"""Please provide me the following in JSON format:

- "personal_details" which should include: name, location, phone, email, LinkedIn, and GitHub.
- "education" should be categorized as school/university, duration_years, GPA, courses.
- "experience" should be categorized as company_name, duration, and summary which should contain any information that has been provided under any role.
-  Keep the summary as it is, and don't change anything.
- "projects" should be organized similarly to "experience" where it should be divided into title, duration, skills, and summary.
    Skills should contain all technical skills, languages, frameworks, tools, and databases used in the project.
    Summary should contain any information that has been provided under any project. keep it as it is without changing anything
- "technical_skills" has different sections like languages, frameworks, tools, databases.
- Add "course_work" section containing courses if only the courses are not mentioned in "education"
- "extra_curriculars," if any, should be sorted into "summary" containing the exact information.
- If any information provided in the resume doesn't fall under one of the above categories,
  include these sections in "others." Include each section under the name of the section.

Do not include any information twice.

Here is the resume. You will have to parse this into the above-mentioned format:
{resume_txt}
 """
    return [
        {
            "role": "user",
            "content": prompt,
        }
    ]


def get_job_details_messages(job_details_txt):
    prompt =  f""" Please provide me the following in JSON format:
        - Job Title: The role that the job details are about
        - Job Description: A description of the job
        - Prerequisites: The minimum skills required for the job. Please include all necessary requirements for the job.
        - Preferred Qualifications: The skills or requirements that are not necessary but are preferred for the job.Any additional requirements comes under this category.
        - Others: Any other information that you would like to include in the job details.
        Please make sure not to repeat data in multiple fields.

        Here is the text format of the job details.You will have to parse this into the above-mentioned format:
        {job_details_txt}
    """
    return [
        {
            "role": "user",
            "content": prompt,
        }
    ]
