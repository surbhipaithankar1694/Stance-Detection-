import nltk
import csv,sys

file =  open('train.csv','r')
data = []
for line in file:
    data += line.split("\r")

data = data[1:]
print data[0]
tweetdata = [x.split('"') for x in data]

tweetdata = tweetdata[:1]
#print tweetdata[1]

tweets = {}
for every in tweetdata:
    print every[0]
    tweets[every[1]] = tweetdata[every][0]

print tweets
