import PyPDF2

pdfFile = PyPDF2.PdfReader("C:\\activitytest.pdf", strict=False)

key = "/Annots"
uri = "/URI"
ank = "/A"
mylist = []

for page_no in range(len(pdfFile.pages)):
    page = pdfFile.pages[page_no]
    text = page.extract_text()
    pageObject = page.get_object()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            try:
                u = a.get_object()
                if uri in u[ank].keys():
                    mylist.append(u[ank][uri])
                    print(u[ank][uri])
            except KeyError:
                pass
