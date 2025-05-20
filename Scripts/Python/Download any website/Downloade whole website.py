import os
import requests
import pdfkit
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from docx import Document
import threading
from queue import Queue

# Configuration
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
MAX_THREADS = 5
visited_urls = set()
base_url = ""
output_dir = "website_download"
os.makedirs(output_dir, exist_ok=True)

def is_valid(url):
    """Check if URL is valid and belongs to the same domain."""
    parsed = urlparse(url)
    base_parsed = urlparse(base_url)
    return bool(parsed.netloc) and parsed.netloc == base_parsed.netloc

def get_all_links(url):
    """Extract all links from a webpage."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = set()
        for a_tag in soup.find_all('a', href=True):
            link = urljoin(url, a_tag['href'])
            if is_valid(link) and link not in visited_urls:
                links.add(link)
        return links
    except Exception as e:
        print(f"Error getting links from {url}: {e}")
        return set()

def download_page(url, format_type):
    """Download and save a single page in specified format."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response.raise_for_status()
        html_content = response.text
        
        # Create directory structure
        parsed = urlparse(url)
        path = parsed.path.lstrip('/')
        dir_path = os.path.join(output_dir, os.path.dirname(path))
        os.makedirs(dir_path, exist_ok=True)
        
        filename = os.path.join(dir_path, os.path.basename(path) or 'index')
        
        if format_type == 'pdf':
            output_file = f"{filename}.pdf"
            pdfkit.from_string(html_content, output_file, configuration=config)
        elif format_type == 'docx':
            output_file = f"{filename}.docx"
            soup = BeautifulSoup(html_content, 'html.parser')
            doc = Document()
            for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'li']):
                doc.add_paragraph(element.get_text())
            doc.save(output_file)
        else:  # html
            output_file = f"{filename}.html"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
        
        print(f"Saved: {output_file}")
        return True
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return False

def worker(url_queue, format_type):
    """Worker thread for processing URLs."""
    while True:
        url = url_queue.get()
        if url is None:
            break
        
        if url not in visited_urls:
            visited_urls.add(url)
            download_page(url, format_type)
            
            # Get and add new links to queue
            new_links = get_all_links(url)
            for link in new_links:
                if link not in visited_urls:
                    url_queue.put(link)
        
        url_queue.task_done()

def crawl_website(start_url, format_type, max_depth=3):
    """Crawl website starting from given URL."""
    global base_url
    base_url = start_url
    url_queue = Queue()
    url_queue.put(start_url)
    
    # Create worker threads
    threads = []
    for _ in range(MAX_THREADS):
        t = threading.Thread(target=worker, args=(url_queue, format_type))
        t.start()
        threads.append(t)
    
    # Wait for all URLs to be processed
    url_queue.join()
    
    # Stop workers
    for _ in range(MAX_THREADS):
        url_queue.put(None)
    for t in threads:
        t.join()

def main():
    print("Advanced Website to File Converter")
    print("="*40)
    
    url = input("Enter website URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print("\nSelect output format:")
    print("1. PDF")
    print("2. DOCX")
    print("3. HTML")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    format_type = {'1': 'pdf', '2': 'docx', '3': 'html'}.get(choice, 'html')
    
    print("\nCrawling website (this may take a while)...")
    crawl_website(url, format_type)
    print("\nWebsite download complete!")

if __name__ == "__main__":
    main()