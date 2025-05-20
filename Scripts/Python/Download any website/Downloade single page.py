import os
import requests
import pdfkit
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from docx import Document

# Configuration
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
output_dir = "single_page_download"
os.makedirs(output_dir, exist_ok=True)

def download_single_page(url, format_type):
    """Download and save only the specified page."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response.raise_for_status()
        html_content = response.text
        
        # Create filename from URL
        parsed = urlparse(url)
        base_name = parsed.netloc.replace('.', '_') + parsed.path.replace('/', '_')
        if not base_name:
            base_name = "downloaded_page"
        
        if format_type == 'pdf':
            output_file = os.path.join(output_dir, f"{base_name}.pdf")
            pdfkit.from_string(html_content, output_file, configuration=config)
        elif format_type == 'docx':
            output_file = os.path.join(output_dir, f"{base_name}.docx")
            soup = BeautifulSoup(html_content, 'html.parser')
            doc = Document()
            for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'li']):
                doc.add_paragraph(element.get_text())
            doc.save(output_file)
        else:  # html
            output_file = os.path.join(output_dir, f"{base_name}.html")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
        
        print(f"Successfully saved: {output_file}")
        return True
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return False

def main():
    print("Single Page Downloader")
    print("="*30)
    
    url = input("Enter website URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print("\nSelect output format:")
    print("1. PDF")
    print("2. DOCX")
    print("3. HTML")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    format_type = {'1': 'pdf', '2': 'docx', '3': 'html'}.get(choice, 'html')
    
    download_single_page(url, format_type)
    print("\nDownload complete!")

if __name__ == "__main__":
    main()