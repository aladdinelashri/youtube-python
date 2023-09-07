import PyPDF2

pdf = PyPDF2.PdfReader("C:\\My youtube Activity.pdf")

urls = []
for page in range(len(pdf.pages)):
    pdfPage = pdf.pages[page]
    try:
        for item in (pdfPage['/Annots']):
            print(item)
    except KeyError:
        pass
