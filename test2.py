import PyPDF2
import pandas as pd
import pdfminer
import PDFQuery


def extract_links(pdf_file):
  """Extracts hyperlinks from a PDF file that start with the text "watched".

  Args:
    pdf_file: The path to the PDF file.

  Returns:
    A list of hyperlinks.
  """

  pdf = PyPDF2.PdfReader(pdf_file)
  links = []
  for page in pdf.pages:
    analyzer = PyPDF2.pdf.ContentStreamAnalysis(page)
    for link in analyzer.links:
      if link.title.startswith('Watched'):
        links.append(link)

  return links

def write_links_to_excel(links, output_file):
  """Writes hyperlinks to an Excel spreadsheet.

  Args:
    links: A list of hyperlinks.
    output_file: The path to the Excel spreadsheet.

  """

  data = []
  for link in links:
    data.append([link.destination, link.title])

  df = pd.DataFrame(data, columns=['Link', 'Text'])
  df.to_excel(output_file)

if __name__ == '__main__':
  pdf_file = 'C:\\activitytest.pdf'
  output_file = 'links.xlsx'

  links = extract_links(pdf_file)
  write_links_to_excel(links, output_file)
