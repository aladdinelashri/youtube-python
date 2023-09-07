import PyPDF2
import re

pdfFileObject = open("C:\\activitytest.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObject)

for page_number in range(len(pdfReader.pages)):
    pageObject = pdfReader.pages[page_number]
    pdf_text = pageObject.extract_text()
    urls = re.findall(r'(https?://\S+)', pdf_text)
    print(urls)
    for url in urls:
        if 'youtube.com' in url:
            print(url)
            
