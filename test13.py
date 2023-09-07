import PyPDF2

pdfFile = PyPDF2.PdfReader("C:\\activitytest.pdf", strict=False)

key = "/Annots"
uri = "/URI"
ank = "/A"
mylist = set()

for page_no in range(len(pdfFile.pages)):
    page = pdfFile.pages[page_no]
    text = page.extract_text()
    print(f'Extracted text from page {page_no + 1}:')
    pageObject = page.get_object()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            try:
                u = a.get_object()
                if uri in u[ank].keys():
                        link = u[ank][uri]
                        if link.startswith("https://www.youtube.com/watch?v="):
                            if link not in mylist:
                                mylist.add(link)
                                print(link)
            except KeyError:
                    pass

print("The number of unique YouTube links is:", len(mylist))
