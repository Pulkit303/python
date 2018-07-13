#!/usr/bin/python2 

import tweepy
import sys
from textblob import TextBlob
import matplotlib.pyplot as plt

Consumer_key='consumer_key'
Consumer_secret='consumer_secret'

auth=tweepy.OAuthHandler(Consumer_key,Consumer_secret)

Acess_key='Acess_key'
Acess_secret='access_secret'

auth.set_access_token(Acess_key,Acess_secret)

connect = tweepy.API(auth)
x=raw_input("enter here: ")
#get_data=connect.search(x,count=10)
get_data=connect.search(x)
l = []
j = []
for i in get_data:
	analysis=TextBlob(i.text)
	print analysis.sentiment
	polarity=analysis.sentiment.polarity
	sub =analysis.sentiment.subjectivity
	l.append(polarity)
	j.append(sub)

	
plt.xlabel("subjectivity")
plt.ylabel("polarity")
plt.scatter(j,l,marker='*')
plt.plot(j,l)
plt.show()

