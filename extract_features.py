import csv
import nltk

data = []
data1 = []
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


for eachtweet in tweetdata:
    tokens = nltk.word_tokenize(eachtweet[0])
    pos_tokens = nltk.pos_tag(tokens)
   
    for each in pos_tokens:
#        if each[1] in ('JJ','JJR','JJS','NN','NNS','NNP','VB','VBD','VBG','VBN','VBP','VBZ'):
            tweetdir[eachtweet[1]].append(each[0])



for eachtweet in testdata:
    str = ""
    testtokens = nltk.word_tokenize(eachtweet[0])
    if eachtweet[1]=='Donald Trump':
        for word in tweetdir['Hillary Clinton']:
            if word in testtokens:
            #print word,"yes"
                str+= '1,'
            else:
            #print word,"no"
                str+='0,'
        str+= eachtweet[2]
        print str

"""
    
for eachtweet in tweetdata:
    str = ""
    testtokens = nltk.word_tokenize(eachtweet[0])
    if eachtweet[1]=='Hillary Clinton':
        for word in tweetdir[eachtweet[1]]:
            if word in testtokens:
            #print word,"yes"
                str+= '1,'
            else:
            #print word,"no"
                str+='0,'    
        if eachtweet[2]=='FAVOR':
            str+= 'AGAINST'
        elif eachtweet[2]=='AGAINST':
            str+= 'FAVOR'
        else:
            str+= 'NONE'
        print str


"""
