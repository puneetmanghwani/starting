#!/usr/bin/python3
import tweepy
import cursor
consumer_key="bSh5wvnGDnoE0HShQjbLcDCj5"
consumer_secret="mwyr7FEk1z54uqhqxRSnHCoEM9QgdNVfEPNofH6gU3VwIbgfcs"
access_key="2953318536-Pm32gN5okawo4lcZlzpIIxfzvRpAuPWIZcbP9lT"
access_secret="BYzfYILbGoVrCfPt2exw4JBLnDBP8eKWDETOftiO285Ff"


def get_tweets(username): 
          
       
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
      
        auth.set_access_token(access_key, access_secret) 
  
      
        api = tweepy.API(auth) 
  
  
        number_of_tweets=50
        tweets = api.user_timeline(screen_name=username) 
  
  
        tmp=[]

        tmp1=tweepy.Cursor(api.search,input('enter any topic hashtag to be searched'))
  	
      
        tweets_for_csv = [tweet.text for tweet in tweets]  
        for j in tweets_for_csv: 
  
           
            tmp.append(j)  
  
        
        print(tmp) 
        for items in tmp1.items(10):
          print(items.text)
          print('\n')
  	
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
   # data=str(input('enter')) 
 #   print(input('enter'))
    get_tweets(input('enter the username if you want tweets based on it'))
