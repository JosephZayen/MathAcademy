from PyPDF2 import PdfReader
from blueprints.ai_textbook_factory.pdf_plain_text.config import source_path

reader = PdfReader(source_path + r"pdf_plain_text/fluent python.pdf")
text = ''
number_of_pages = len(reader.pages)

for i in range(6,22):
    page = reader.pages[i]
    page_text = page.extract_text()
    text += page.extract_text()

print(text)

with open(source_path + "pdf_plain_text/extract.txt","a",encoding="utf-8") as fh:
    fh.write('\n'*7 + text + '\n'*10)