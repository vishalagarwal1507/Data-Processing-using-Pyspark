from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem import RegexpStemmer
#from gensim import corpora

import os
import string
import sys


class StopWords:
    
    def f_load(self):
        stopwordsFile="stopword.txt"       
        stopwordsFileData=[]        
        with open(stopwordsFile,'r') as stopwrdFile: 
            temp=[]
            while True:
                line = stopwrdFile.readline().split()
                if not line:
                    break
                temp.append(line)
        for sublist in temp:
            for item in sublist:        
                stopwordsFileData.append(item)
        UserDefinedStopwords=set(stopwordsFileData)
        
        stop_words = set(stopwords.words("english"))  	# assigning variable and load stopwords
        punc_words = set(string.punctuation)		# assigning variable and load punctuation
        nouse_words=stop_words | punc_words | UserDefinedStopwords		# combining stopwords and punctuation and UserDefinedStopwords

        #lmtzr = WordNetLemmatizer()			# assigning variable lemmatization word
        #snowball_stemmer = SnowballStemmer("english")	# assigning variable stemming word
        
        return(nouse_words)