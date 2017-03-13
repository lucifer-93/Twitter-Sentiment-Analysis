
# coding: utf-8

# In[ ]:

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import tweepy


#consumer key, consumer secret, access token, access secret.


ckey='0wZojBRTUQZMuc8Srl8Z4hu9i'
csecret='mziWSJdh06dHcISHW9o6yrpqk2QGai54wRLqT90LutMGXQqOTo'
atoken='833809580496805889-PYsLUVNtdQ7uYH7hpTU9m3n66sGMOD3'
asecret='MvpU1x1ZlpVLC2NRm2okzfccNzZXfabyWdaqNK7a1QMof'

class listener(StreamListener):

    def on_data(self, data):
        
        tweet=data.split(',"text":"')[1].split('","source')[0]
        cleanFile=str(time.time())+'::'+tweet
        file=open('RefugeeCleanedFile.txt','a')
        file.write(cleanFile)
        file.write('\n')
        file.close()
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['#TravelBan','#refugee','#immigrants','#muslimban'])


# In[ ]:



