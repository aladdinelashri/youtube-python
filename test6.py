import fitz
import re

def get_youtube_links(pdf_file):
    """Get all YouTube links from a PDF file."""
    doc = fitz.open(pdf_file)
    links = []
    for i in range(doc.page_count):
        page = doc.load_page(i)
        for link in page.get_links():
            if isinstance(link, str) and link.startswith("https://www.youtube.com/watch?"):
                match = re.match(r"https://www.youtube.com/watch?=(.*)", link)
                if match:
                    links.append(match.group(1))
    return links


pdf_file = "C:\\activitytest.pdf"
links = get_youtube_links(pdf_file)
print(links)