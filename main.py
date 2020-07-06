import urllib.request
import json

channel_name = input("Enter Youtube channel name: ")
key =  "AIzaSyDHVol6r4EEtiGe2rmUrTl-HndlpAHriWo" #Enter your api key
try:
    url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+channel_name+"&key="+key

    data = urllib.request.urlopen(url).read()
    sub_count = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
except:
    print("Invalid channel name !!!")
print(f"{channel_name} subcribers count is : {sub_count}")


