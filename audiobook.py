import pyttsx3
import PyPDF2
from pdf2text import text

book = open('Untitled.pdf', 'rb')
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "b" - Binary - Binary mode (e.g. images)
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
TTSapp = pyttsx3.init()
TTSapp.setProperty('rate', 120)
for num in range(0, pages):
    # You can set the range of pages.
    page = pdfReader.getPage(num)
    text_in_page = page.extractText()
    print(text_in_page)
    TTSapp.say("Let's start to read page {} .".format(num))
    TTSapp.say(text)
    TTSapp.runAndWait()
    TTSapp.stop
