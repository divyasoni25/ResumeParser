# Resume Parser

This project extracts text from a resume PDF and parses it into a JSON format using OpenAI's GPT-3.5-turbo model.

## Requirements

- PyMuPDF (`fitz`)
- OpenAI Python package

  ```

## Usage

1. Set your OpenAI API key in the `assignment.py` file:
    ```python
    openai.api_key = 'YOUR_API_KEY'
    ```
2. Place your resume PDF in the project directory and name it `resume.pdf`.
3. Run the script:
    ```bash
    python assignment.py
    ```

## Output

The script will print the parsed JSON content of the resume.

## Example

An example resume PDF is included in the repository. You can test the script using this file.

