##############################
#### Word Cloud with Wikipedia
#### pip install wikipedia
### pip install numpy
### pip install wordcloud
### pip install Pillow
#### you have to run this code on terminal or cmd
##############################

import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np

currdir = os.path.dirname(__file__)

def get_wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

def create_wordcloud(text):
    mask = np.array(Image.open(os.path.join(currdir, "black.jpg")))
    stopwords = set(STOPWORDS)

    word_cloud = WordCloud(background_color='white',
                            mask = mask,
                            max_words=400,
                            stopwords=stopwords)
    word_cloud.generate(text)       

    word_cloud.to_file(os.path.join(currdir, "wordcloud.png"))                 

# You can change the 'Python Programming Language' expression in the line below as you wish
create_wordcloud(get_wiki("Python Programming Language"))
