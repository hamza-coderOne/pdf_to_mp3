
import pyttsx3
import pdfplumber
import PyPDF2






def convertPdfToMp3(pdf, mp3):
    file = pdf

    f = open(file, "rb")
    pdfR = PyPDF2.PdfFileReader(f)
    pages = pdfR.numPages

    with pdfplumber.open(file) as pdf:
      for i in  range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            print(text)
            s = pyttsx3.init()
            s.save_to_file(text, mp3)
            s.runAndWait()


    f.close()

convertPdfToMp3("your pdf file", "your new mp3 file name")
