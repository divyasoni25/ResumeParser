import fitz  # PyMuPDF
import openai

# Define your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def parse_resume_to_json(resume_text):
    prompt = f"""
    Given the text of a resume from a PDF, parse it into JSON format with the following structure:
    {{
        "Name": "",
        "Contact Information": {{
            "Email": "",
            "Phone": "",
            "LinkedIn": ""
        }},
        "Education": [
            {{
                "Institution": "",
                "Degree": "",
                "Field of Study": "",
                "Start Date": "",
                "End Date": ""
            }}
        ],
        "Experience": [
            {{
                "Position": "",
                "Company": "",
                "Start Date": "",
                "End Date": "",
                "Responsibilities": [""]
            }}
        ],
        "Skills": [""]
    }}. Input: {resume_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500
    )

    return response.choices[0].message["content"].strip()

# Example usage
pdf_path = 'resume.pdf'
resume_text = extract_text_from_pdf(pdf_path)
parsed_resume = parse_resume_to_json(resume_text)
print(parsed_resume)
