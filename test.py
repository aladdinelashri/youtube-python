import PyPDF2
import pandas as pd

def extract_links(pdf_file):
  """Extracts hyperlinks from a PDF file.

  Args:
    pdf_file: The path to the PDF file.

  Returns:
    A list of hyperlinks.
  """

  pdf = PyPDF2.PdfReader(pdf_file)
  links = []
  for page in pdf.pages:
    links.extend(page.get_links())

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
  pdf_file = 'activitytest.pdf'
  output_file = 'links.xlsx'

  links = extract_links(pdf_file)
  write_links_to_excel(links, output_file)
