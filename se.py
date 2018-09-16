from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize  

file = "python.txt"                  
file = open(file,"r")                   #Reading file
for line in file:                       #Extracting File
    print (line)
str = input("What you want to search: ")

stop_words = set(stopwords.words('english'))  #stopwords
word_tokens = word_tokenize(str)  
filtered_sentence = [w for w in word_tokens if not w in stop_words]  
filtered_sentence = []  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print ("Stopword is : ")
print(filtered_sentence)


#ps = PorterStemmer()                     #Stemming
#ps.stem(filtered_sentence)
#print ("Stemmed is : ")
#print(filtered_sentence)

data = open('python.txt').read()
count = data.count(str)                    #frequency

print(count)
file.close()

