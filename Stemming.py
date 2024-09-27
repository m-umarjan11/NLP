import nltk
paragraph = """
Born in Lahore, Khan graduated from Keble College, Oxford. He began his international cricket career in a 1971 Test series against England. Khan played until 1992, served as the team's captain intermittently between 1982 and 1992, and won the 1992 Cricket World Cup, Pakistan's only victory in the competition. Considered one of cricket's greatest all-rounders, Khan was later inducted into the ICC Cricket Hall of Fame. Founding the Pakistan Tehreek-e-Insaf (PTI) in 1996, Khan won a seat in the National Assembly in the 2002 general election, serving as an opposition member from Mianwali until 2007. PTI boycotted the 2008 general election and became the second-largest party by popular vote in the 2013 general election. In the 2018 general election, running on a populist platform, PTI became the largest party in the National Assembly, and formed a coalition government with independents with Khan as prime minister."""
from nltk import PorterStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    stemmed_words = [stemmer.stem(word) for word in words]
    print(stemmed_words)


