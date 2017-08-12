import requests
import json
import csv
import pickle
import random



api_key = "AIzaSyDraPMr8KRfkux5u9DgCjfWh1SA_xJmIl8"
test_api_key = "AIzaSyD1fGnUYGPjdfpklW9PmjbQkOqlUKxQ3o8"

url = "https://www.googleapis.com/youtube/v3/search?key="+test_api_key+"&type=video&part=snippet&q=bathing" \
                                                                       "&maxResults=50"

r = requests.get(url=url)

#print(r)
raw_data = r.json()

item_list = raw_data["items"]

idsfile = open('videoandchannelid.csv', "a")
heading = ("videoId", "channelId")
video_channel_id = []
#print(item_list)


for item in item_list:
    ids = {}
    #print(item.keys())
    #print(item["id"]["videoId"], end=" ")
    #print(item["snippet"]["channelId"])
    ids["videoId"] = item["id"]["videoId"]
    ids["channelId"] = item["snippet"]["channelId"]
    print(ids)
    video_channel_id.append(ids)


print(video_channel_id)
bridge = csv.DictWriter(idsfile, heading)
for row in video_channel_id:
    bridge.writerow(row)
