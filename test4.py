# Import necessary packages
import PyPDF2
import re

file = open("C:\\My youtube Activity.pdf", 'rb')
readPDF = PyPDF2.PdfReader(file)
def find_url(string):
   #Find all the String that matches with the pattern
   regex = r"(https?://\S+)"
   url = re.findall(regex,string)
   for url in url:
      return url
# Iterating over all the pages of File
for page_no in range(len(readPDF.pages)):
   page=readPDF.pages[page_no]
   #Extract the text from the page
   text = page.extract_text()
   # Print all URL
   print(find_url(text))
# CLost the file
file.close()
