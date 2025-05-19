# Add this at the top if your wkhtmltopdf isn't in system PATH
config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')
pdfkit.from_string(html, output_file, configuration=config)
import os
import requests
import pdfkit
from docx import Document
from bs4 import BeautifulSoup

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
        pdfkit.from_string(html_content, output_file)
        print(f"Successfully saved as PDF: {output_file}")
    except Exception as e:
        print(f"Error creating PDF: {e}")

def save_as_docx(html_content, output_file):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        doc = Document()
        for paragraph in soup.find_all('p'):
            doc.add_paragraph(paragraph.get_text())
        doc.save(output_file)
        print(f"Successfully saved as DOCX: {output_file}")
    except Exception as e:
        print(f"Error creating DOCX: {e}")

def save_as_html(html_content, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Successfully saved as HTML: {output_file}")
    except Exception as e:
        print(f"Error creating HTML: {e}")

def main():
    print("Website to File Converter")
    print("="*30)
    
    url = input("Enter website URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print("\nSelect output format:")
    print("1. PDF")
    print("2. DOCX")
    print("3. HTML")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    html_content = get_website_content(url)
    if not html_content:
        return
    
    base_name = url.split('//')[-1].replace('/', '_').replace('.', '_')
    
    if choice == '1':
        output_file = f"{base_name}.pdf"
        save_as_pdf(html_content, output_file)
    elif choice == '2':
        output_file = f"{base_name}.docx"
        save_as_docx(html_content, output_file)
    elif choice == '3':
        output_file = f"{base_name}.html"
        save_as_html(html_content, output_file)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()