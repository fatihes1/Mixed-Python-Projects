#####################################################
#### Text to Speech with Python
#### pip install gTTS
#### you have to run this code on terminal or cmd
#####################################################
from gtts import gTTS # we have import this module for text to speech conversion
import os


text = "Hello guys. Let's learn Python and have fun." # you can change this text

language = 'en' # for English language

obj = gTTS(text=text, lang=language, slow=False)
# we have used slow = False because our converted video will have a high speed

obj.save("sample.mp3")

# to open the auido file automatically we have to import os
os.system("sample.mp3")

