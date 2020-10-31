from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import pyttsx3

Speaker = pyttsx3.init()
Speaker.setProperty('rate', 120)
output_string = StringIO()
with open('Untitled.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    page_num = 1
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
        print(page)
        Speaker.say("Let's start to read page {}".format(page_num))
        print(output_string.getvalue())
        Speaker.say(output_string.getvalue())
        Speaker.runAndWait()
        Speaker.stop
        page_num += 1
