from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer

stp_words = stopwords.words('english')

def Tokenize(txt):
    return word_tokenize(txt)

def RemoveStopWords(txt):
    text_without_stop_words = []

    for word in txt:
        word = word.lower()
        if word not in stp_words:
            text_without_stop_words.append(word)
    
    return text_without_stop_words

def Lemmatize(word):    
    wl = WordNetLemmatizer()
    return wl.lemmatize(word)

def Stemmed(word):
    ls = LancasterStemmer()
    return ls.stem(word)


if __name__ == '__main__':
    print("Main Program.")