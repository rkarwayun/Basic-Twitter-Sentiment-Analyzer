import tweepy
import csv
from textblob import TextBlob

#Authentication
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#Getting Search Word and Number of Tweets to analyze from the user
print("Input the search word")
searchword = input()

print("Enter number of tweets that you want to analyze")
number = input()
number = int(number)


#Getting the required number of tweets with the search word
tweets_all = api.search(searchword, count = number)


#Now let's analyze some tweets!
counter = 0
sum = 0

with open('tweets.csv', 'w', encoding='utf=8') as csvFile:
    writer = csv.writer(csvFile)
    row = ['Tweet', 'Sentiment (Positive or Negative)']
    writer.writerow(row)

    for tweet in tweets_all:
        #print(tweet.text)

        counter = counter + 1
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment)
        sum = sum + analysis.polarity
        if analysis.polarity >= 0.05:
            sentiment = 'Positive'
        else:
            sentiment = 'Negative'
        row1 = [tweet.text, sentiment]
        writer.writerow(row1)


print("Overall Sentiment is:")
print(sum/counter)
if sum/counter >= 0.05:
    print("Positive")
else:
    print("Negative")