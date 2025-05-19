import os
import requests
import pdfkit  # ADD THIS IMPORT
from docx import Document
from bs4 import BeautifulSoup

# Use raw string for Windows path
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

def get_website_content(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching website: {e}")
        return None

def save_as_pdf(html_content, output_file):
    try:
        pdfkit.from_string(html_content, output_file, configuration=config)  # Add config here
        print(f"Successfully saved as PDF: {output_file}")
    except Exception as e:
        print(f"Error creating PDF: {e}")

# ... [rest of your existing functions] ...

if __name__ == "__main__":
    main()