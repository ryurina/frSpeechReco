#coding:utf-8

import speech_recognition as sr
import os

print("AUDIO TRANSCRIPTION\nAuthor: RANARISON Rina\nVersion: 1.0 (VF seulement)\nGithub : https://github.com/ryurina/frSpeechReco\n\n")

def reconnaissance():
    while True:
        r = sr.Recognizer()

        audiofile = input("[+] Entrer '.wav' fichier seulement: ")

        sound = sr.AudioFile(audiofile)

        with sound as source:
            audio = r.record(source)

        transcripted = r.recognize_google(audio, language="fr-FR")
        data = str(transcripted)

        file = open('data.txt', 'w')
        file.write(data)
        file.close()

        print("[!] Transcription fini / output:'data.txt' \n")

        user = int(input('Tapez: \n0 - Quitter\n1 - Transcrire un autre fichier\nUtilisateur : '))
        if(user == 0):
            print("Merci! d'avoir utiliser mon programme! ")
            break
            os.system("pause")
        else:
            pass
reconnaissance()
