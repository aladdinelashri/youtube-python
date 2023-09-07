import pdfplumber

def extract_youtube_urls(pdf_file):
  """Extracts all YouTube URLs from a PDF file.

  Args:
    pdf_file: The path to the PDF file.

  Returns:
    A list of YouTube URLs.
  """

  pdf_obj = pdfplumber.open(pdf_file)
  urls = []
  for page in pdf_obj.pages:
    for link in page.annots:
      if "Link" in link:
        if "youtube.com" in link.get("URI"):
          urls.append(link.get("URI"))
        else:
          print(link)

  return urls


if __name__ == "__main__":
  pdf_file = "youtube_activity.pdf"
  pdf_file = "activitytest.pdf"
  urls = extract_youtube_urls(pdf_file)
  print(urls)
