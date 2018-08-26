# Data-Processing-using-Pyspark
In this project, the goal is to preprocess the text data using distributed processing functinality of Pyspark.

In pyspark instead of using the resilient distributed datasets we have focused on using pyspark dataframe which are very similar to pandas dataframe. The main difference is that pyspark dataframe could be distributed on the worker node and hence quite helpful for processing large volume of data.

### Some Basic Preprocessing functionality-

In this project a custom transformer has been implemented which could take different stopwords lemmatization and other parameters and provides lazy loading functionality.

The user defined stopwords punctuation and names can be easily removed by adding it to the stopwords.txt file.

The replacement with root word i.e. lemmatization functionality has also been added which could help in some particular use cases.

The removal of words with length less then 2 (this count can be changed in the StopWordsLoad.py python script)

There are two stemmer used -
  a)Snowbell Stemmer- It is in-built in python. 
  b)Regex Stemmer- It is a custom stemmer which can take input from the regex.txt file.
  Any of these can be used.

The preprocessed data can be saved in a file or the database.

### Feature conversion from text.

The preprocessed text can be converted in features using various technique for some further analysis.
One of such technique is bag of words.
In this technique all the words are split in token and assigned a number and saved in dictionary then each document is converted into bag of words from that dictionary, which is having a word to number mapping. 

### Features to Model Building.
These features can be used for making a model.
One implementation of such model can be seen in the notebook.
Latent Dirichlet Allocation is used for topic modelling.
The visualization for the output has been added in the LDAvis.png file.
  
