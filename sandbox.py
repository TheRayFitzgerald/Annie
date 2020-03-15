import pandas as pd
import json
"""
with open('all_text.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print(p['subreddit'])
"""
json_objects=[]
with open('./corpora/RC_2015-01', 'r') as file:

    for i in range(9999):
        json_objects.append(json.loads(file.readline()))
        #print(file.readline())

print(json_objects)
for p in json_objects:
    print(p['subreddit'])