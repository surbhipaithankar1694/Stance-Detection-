import csv
import nltk

data = []
data1 = []
data2 = []
data3 = []
lexicon_dic = {}
word1 = []
polarity1 = []
with open('train2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

with open('test2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data1.append(row)

tweetdata = data[1:]
testdata = data1[1:]
tweetdir = {}


for every in tweetdata:
    tweetdir[every[1]] = []

lexfile =  open('subjclueslen1-HLTEMNLP05.tff','r')
for line in lexfile:
        data2 +=line.split("\n")
data3+=[x.split(' ') for x in data2]
for each in data3:
    if each == ['']: 
        data3.remove(each)
stemmer = nltk.PorterStemmer()


for eachline in data3:
    word =  eachline[2]
    word1 = word.split('=')
    polarity = eachline[5]
    polarity1 = polarity.split('=')
    lexicon_dic[word1[1]] = polarity1[1]

#print lexicon_dic

str=""


for eachtweet in tweetdata:
  if eachtweet[1] == "Hillary Clinton":
    str = ""
    tokens = nltk.word_tokenize(eachtweet[0])
    stems = [stemmer.stem(word) for word in tokens]
    for each in lexicon_dic.keys():
        if each in stems:
            polarity = lexicon_dic[each]
        else:
            polarity = "neutral"
        if polarity == "positive":
            str += '1,'
        elif polarity == "negative":
            str += '-1,'
        elif polarity == "neutral":
            str += '0,'
    if eachtweet[2] == "Favor":
        str += "Against"
    elif eachtweet[2] == "Against":
        str += "Favor"
    else:
        str += "NONE"
    print str
    print "\n"
"""    

for eachtweet in testdata:
  if eachtweet[1] == "Donald Trump":
    str = ""
    tokens = nltk.word_tokenize(eachtweet[0])
    stems = [stemmer.stem(word) for word in tokens]
    for each in lexicon_dic.keys():
        if each in stems:
            polarity = lexicon_dic[each]
        else:
            polarity = "neutral"
        if polarity == "positive":
            str += '1,'
        elif polarity == "negative":
            str += '-1,'
        elif polarity == "neutral":
            str += '0,'
    str += eachtweet[2]
    print str

 
"""
