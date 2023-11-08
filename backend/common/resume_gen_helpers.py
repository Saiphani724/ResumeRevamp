def get_resume_gen_messages(resume_json, job_json):
    prompt = f"""
        -here id the json format of the resume {resume_json}
        - Never add extra information to the resume details.
        - Make use of the job_details {job_json} and use it according to the description provided in the prompt.
        - Try to optimize the resume according to the job_details.
        - gpa in education if provided out of 10, convert it to 4 using WES GPA calculator.
        - summary of the "experience" should be optimised according to the prerequisites and preferred qualifications from job_details.
        - If there are too many sections in experience, include only the experience details that are relevant to the job_details.
        - "projects" should be organized similarly to "experience."
        -  Organise "technical_skills" with respect to job_details.
    """

    messages = [
        {
            "role": "system",
            "content": "extract details from resume and convert them into required format using the function extract_details ",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]
    
    return messages


resume_gen_functions = [
    {
        "name": "revamp_resume",
        "description": "Extract the details from the resume_json and convert them into required format.",
        "parameters": {
            "type": "object",
            "properties": {
                "personal_details": {
                    "type": "object",
                    "description": "All perssonal details of the candidate must be present in this section, if some details are extra than mentioned in the prompt, add them using camel_case with appriopriate description",
                    "properties": {
                        "name": {"type": "string"},
                        "location": {
                            "type": "string",
                            "description": "City, State, Country",
                            "example": "New York, NY, USA",
                        },
                        "phone": {
                            "type": "string",
                            "description": "Phone number with country code",
                            "example": "+1 123 456 7890",
                        },
                        "email": {
                            "type": "object",
                            "description": "Email address, if there are more than one email address divide them by using commas",
                            "example": "vankitreddy@gmail.com, ritvik@gmail.com",
                        },
                        "linkedin": {
                            "type": "string",
                            "description": "LinkedIn profile URL",
                            "example": "https://www.linkedin.com/in/ankit-reddy-v-7b1b1b1b1/",
                        },
                        "github": {
                            "type": "string",
                            "description": "GitHub profile URL",
                        },
                        "portfolio": {"type": "string", "description": "Portfolio URL"},
                    },
                    "required": ["name", "location", "phone", "email"],
                },
                "education": {
                    "type": "array",
                    "items": {
                        "description": "All education details of the candidate must be present in this section",
                        "properties": {
                            "university": {
                                "type": "string",
                                "description": "university name",
                            },
                            "duration_years": {
                                "type": "string",
                                "description": "Duration of education in years",
                            },
                            "gpa": {
                                "type": "string",
                                "description": "GPA of the candidate, if the GPA is provided out of 10, convert it to 4 using WES GPA calculator",
                            },
                            "courses": {
                                "type": "string",
                                "description": "Courses taken",
                            },
                        },
                    },
                },
                "experience": {
                    "type": "array",
                    "items": {
                        "description": "All experience details of the candidate must be present in this section",
                        "properties": {
                            "company_name": {
                                "type": "string",
                                "description": "Company name",
                            },
                            "duration": {
                                "type": "string",
                                "description": "Duration of work",
                            },
                            "summary": {
                                "type": "string",
                                "description": "Summary of work in 3-4 lines make sure you don't add any extra details",
                            },
                        },
                        "required": ["company_name", "duration", "summary"],
                    },
                },
                "projects": {
                    "type": "array",
                    "items": {
                        "description": "All projects/research details of the candidate must be present in this section",
                        "properties": {
                            "project_name": {
                                "type": "string",
                                "description": "Project name",
                            },
                            "duration": {
                                "type": "string",
                                "description": "Duration of project/research",
                            },
                            "summary": {
                                "type": "string",
                                "description": "Summary of work in 3-4 lines make sure you don't add any extra details",
                            },
                        },
                    },
                },
                "technical_skills": {
                    "type": "object",
                    "description": "All technical skills of the candidate must be present in this section, if some details are extra than mentioned in the prompt, add them using camel_case with appriopriate description and make sure you don't add any extra details also don't add any section if you don't have any details for that section eg: if you don't have any tools known don't add tools section",
                    "properties": {
                        "languages": {
                            "type": "string",
                            "description": "Languages known",
                        },
                        "frameworks": {
                            "type": "string",
                            "description": "Frameworks known",
                        },
                        "tools": {"type": "string", "description": "Tools known"},
                        "databases": {
                            "type": "string",
                            "description": "Databases known",
                        },
                    },
                },
                "course_work": {
                    "type": "object",
                    "description": "All course work details of the candidate must be present in this section, if some details are extra than mentioned in the prompt, add them using camel_case with appriopriate description",
                    "properties": {
                        "courses": {"type": "string", "description": "Courses taken"},
                    },
                },
                "extra_curriculars": {
                    "type": "object",
                    "description": "All extra curriculars details of the candidate must be present in this section, if some details are extra than mentioned in the prompt, add them using camel_case with appriopriate description",
                    "properties": {
                        "extra_curriculars": {
                            "type": "string",
                            "description": "Extra curriculars",
                        },
                    },
                },
            },
        },
    }
]
