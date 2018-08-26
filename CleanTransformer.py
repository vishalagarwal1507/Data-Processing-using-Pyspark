import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer 
from nltk.stem.wordnet import WordNetLemmatizer
from pyspark import keyword_only  ## < 2.0 -> pyspark.ml.util.keyword_only
from pyspark.ml import Transformer
from pyspark.ml.param.shared import HasInputCol, HasOutputCol, Param
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType

              
class CleanTransformer(Transformer, HasInputCol, HasOutputCol):

    @keyword_only
    def __init__(self, inputCol=None, outputCol=None, stopwords=None):
        super(CleanTransformer, self).__init__()
        self.stopwords = Param(self, "stopwords", "")
        self._setDefault(stopwords=set())
        kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, inputCol=None, outputCol=None, stopwords=None):
        kwargs = self.setParams._input_kwargs
        return self._set(**kwargs)

    def setStopwords(self, value):
        self._paramMap[self.stopwords] = value
        return self

    def getStopwords(self):
        return self.getOrDefault(self.stopwords)

    def _transform(self, dataset):
        stopwords = self.getStopwords()

        def f(s):
            if s is not None:
                line = s.lower().replace('"', ']').replace('\'', ' ')			# converting words in lowercase
                tokenized_words = word_tokenize(line)					# tokenizing

                regexFile="regex.txt"
                Snowballstemmer=SnowballStemmer("english")

                RegexStemmer=[]                                #Stemmer for Regular expression
                with open(regexFile,'r') as regFile: 
                    while True:
                        line = regFile.readline()
                        print(line)
                        if not line:
                            break
                        RegexStemmer=RegexpStemmer(line,min=2)

                data =filter(lambda x: x not in stopwords, tokenized_words)		# data=[tokenized_words - nouse_words]
                lmtzr = WordNetLemmatizer()
                list_of_words=[]
                for item in data:
                    if len(item)>2:							# words with length <=2 are removed
                        #rlemma=lmtzr.lemmatize(item)				# lemmatizing				
                        # stemming
                        x=RegexStemmer.stem(item)
                        #x=Snowballstemmer.stem(regx)

                        if len(x)>2:
                            list_of_words.append(x)					# adding item to list_of_words

                t = ' '.join(str(item) for item in list_of_words)
                return t
            
        t = StringType()
        out_col = self.getOutputCol()
        in_col = dataset[self.getInputCol()]
        return dataset.withColumn(out_col, udf(f, t)(in_col))