import pyttsx3                          # offline text-to-speech library
import PyPDF2                           # PDF parser/reader library
from tkinter.filedialog import *        # pulls file-dialog helpers into global namespace

book = askopenfilename(title="Select a PDF", filetypes=[("PDF files", "*.pdf")])       # returns the chosen file path as a string
if not book:
    raise SystemExit("No file selected.")

reader = PyPDF2.PdfReader(book)      # PDF reader object for the selected file
engine = pyttsx3.init()

for i in range(len(reader.pages)):   # loops over pages, extracts text, and runs TTS event loop
    page = reader.pages[i]
    text = page.extract_text() or ""
    if text.strip():
        engine.say(text)

engine.runAndWait()