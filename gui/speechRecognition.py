from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import speech_recognition as sr

# main window
root = Tk()
root.geometry("350x400")
root.resizable(False, False)

# speech recognition function
def reconnaissance():
        r = sr.Recognizer()
        sound = sr.AudioFile(audiofile)
        with sound as source:
            audio = r.record(source)

        transcripted = r.recognize_google(audio, language="fr-FR")
        data = str(transcripted)

        file = open('data.txt', 'w')
        file.write(data)
        file.close()

        state = ttk.Label(root, text ="\n\nFinished!!!",foreground="green", font=("Helvetica", 16))
        state.pack()

        resultwin = Tk()
        resultwin.geometry("600x400")
        resultwin.resizable(False, False)
        resultwin.title("Data.txt")
        datatext = Text(resultwin)
        datatext.insert(INSERT, transcripted)
        datatext.pack()

# Open .wav file menu
def OpenFile():
    global audiofile
    audiofile = askopenfilename(initialdir="",
                           filetypes =(("Audio File", "*.wav"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    label = ttk.Label(root, text =audiofile,foreground="red", background="white",font=("Helvetica", 16))
    label.pack()

# help menu
def aboutApp():
    helv = Font(family='Helvetica', size=30, weight=BOLD)
    paragraph = "\nThis is a simple speech recognization done with python\nOfficial repository : https://github.com/ryurina/frSpeechReco\n\nHOW TO USE IT:\n"
    howtouse = "\nStep 1:\nClick 'File' then 'Open'\n\nStep 2:\nChoose '.wav' file that you want to transcript\n\nStep 3:\nClick 'Transcript' and wait for the result\n\n------------------------------------------\nENJOY FREE AND OPENSOURCE SOFTWARE"
    about =  Tk()
    about.geometry("650x460")
    about.resizable(False, False)
    text = Text(about)
    text.insert(INSERT, "Welcome to SpeechReco FR")
    text.insert(INSERT, paragraph)
    text.insert(INSERT, howtouse)
    text.pack()
    exitBtn = Button(about,foreground='white',background="black",height=2, width=650, text="Exit", command=about.quit)
    exitBtn.pack()

Title = root.title( "SpeechReco FR")

addFile = Button(root,foreground='white',background='black',height=2,width=400, text="Add file", command=OpenFile)
addFile.pack()

# button to launch transcription
transcriptButton = Button(root,foreground='white',background='black',height=2,width=400, text="Transcript", command=reconnaissance)
transcriptButton.pack()

exitButton = Button(root,foreground='white',background='black',height=2,width=400, text="Exit", command=root.quit)
exitButton.pack()

label1 = ttk.Label(root, text ="\n\nFile:\n",foreground="black",font=("Helvetica", 16))
label1.pack()


# menu bar
menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())

about = Menu(menu)
about.add_command(label= "About", command = aboutApp)

menu.add_cascade(label = 'File', menu = file)
menu.add_cascade(label = 'Help', menu = about)


root.mainloop()
