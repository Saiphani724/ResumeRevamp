import json

def get_resume_latex_gen_messages(resume_new):
    system_message = '''
        generate proper latex resume using the given json resume.
        Don't skip anything that is present in the json resume.
        Keep it as compact as possible. Try to fit everything in one page. 
        Use the space wisely. Adjust the font size and margins accordingly. 
        If the content is too long for a single page use reduce the font size and margins, but make sure that the content is readable.
        No overlaps should be there in the resume. 
        Do not add any comments in the start or end or anywhere in the latex resume.
        Compiling that should give a proper pdf.
        give the output latex as a string. DO NOT ADD ANY quotes in the start or end of the latex resume.
    '''
    return [
        {
            "role": "system",
            "content": system_message,
        },
        {
            "role": "user",
            "content": "Here is the resume json: " + json.dumps(resume_new),
        },
    ]