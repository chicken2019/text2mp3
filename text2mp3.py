import os
import sys
from gtts import gTTS

fo = open("text.txt", "r")
text_list = []
lines = fo.readlines()

for line in lines:
    text_list.append(line.replace('\n', ''))
fo.close()
print(text_list)

#Saving part starts from here 
for txt in text_list:
    tts = gTTS(text=txt, lang='ja')
    tts.save(txt+".mp3")
    print("File saved!")
