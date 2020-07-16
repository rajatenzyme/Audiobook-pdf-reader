import pyttsx3
import PyPDF2

book = open('monk.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
#print(voices)
speaker.setProperty('voice', voices[0].id) 
#speaker.setProperty("languages", 'hi')
playback_speed = int(input("Enter Playback Speed: 1 / 1.25 / 1.50 or whatever you want \n"))
speaker.setProperty('rate', (playback_speed + 0.5) * 100)
x = int(input("Enter starting page \n"))
for num in range(x-1 ,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text.encode('utf-8'))
    speaker.say(text)
    speaker.runAndWait()

