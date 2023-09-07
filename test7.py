import pikepdf
import re

pdf_file = pikepdf.Pdf.open("C:\\activitytest.pdf")
urls = []
for page in pdf_file.pages:
    for annots in page.get('/Annots'):
        uri = annots.get('/A').get('/URI', None)
        if uri is not None and type(uri) in (dict, pikepdf.Stream):
            if 'youtube.com' in uri:
                urls.append(uri)
print(urls)