import pyttsx3                          # offline text-to-speech library
import PyPDF2                           # PDF parser/reader library
from tkinter.filedialog import *        # pulls file-dialog helpers into global namespace

book = askopenfilename()                # returns the chosen file path as a string
pdfreader = PyPDF2.PdfReader(book)      # PDF reader object for the selected file
pages = len(pdfreader.pages)            # Counts how many pages are in the PDF

for num in range(0, pages):             # loops over pages, extracts text, and runs TTS event loop
    page = pdfreader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()