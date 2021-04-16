##################################################
#### Word Cloud  with Python
#### pip install matplotlib
#### pip install wordcloud
#### pip install numpy
#### pip install Pillow
#### you have to run this code on terminal or cmd
##################################################


import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

# You can paste the text you want into file 'test.txt' and save it.
dataset = open("test.txt", "r", encoding="utf8").read()
def create_word_cloud(string):
   maskArray = np.array(Image.open("white.png"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.png")
dataset = dataset.lower()
create_word_cloud(dataset)