import requests
import json
import csv
import pickle
import random



api_key = "AIzaSyDraPMr8KRfkux5u9DgCjfWh1SA_xJmIl8"
test_api_key = "AIzaSyD1fGnUYGPjdfpklW9PmjbQkOqlUKxQ3o8"

url = "https://www.googleapis.com/youtube/v3/search?key="+test_api_key+"&type=video&part=snippet&q=boating%7Csailing" \
                                                                       "&maxResults=50"

r = requests.get(url=url)

#print(r)
raw_data = r.json()

item_list = raw_data["items"]

print(len(item_list))
