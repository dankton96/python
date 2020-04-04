import os
import speech_recognition as sr
import datetime
import easygui
numList=['0','1','2','3','4','5','6','7','8','9']
letterList=['a','b','c','d','e','f','g','i','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
FilePath=easygui.fileopenbox("Selecione o arquivo a ser manipulado:")
print(FilePath)
w=FilePath.split("\\")
FilePath=w[-1]
#print(w)
#file=open(FilePath,'r+')
print("\n\nconverting files:\n\n")
command2mp3="ffmpeg -i "+FilePath+" "+FilePath[:-4]+".mp3"
command2wav="ffmpeg -i "+FilePath[:-4]+".mp3 "+FilePath[:-4]+".wav"
os.system(command2mp3)
os.system(command2wav)
print("\n\nloading converted files:\n\n")
########################PROBLEM HERE!!!#########################################
r = sr.Recognizer()
audio = sr.AudioFile(FilePath[:-4]+".wav")
with audio as source:
    audio = r.record(audio)
print(r.recognize_google(audio))
########################PROBLEM HERE!!!#########################################
