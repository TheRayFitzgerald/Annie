import pandas as pd
import json
import string
"""
with open('all_text.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print(p['subreddit'])

json_objects=[]
with open('./corpora/RC_2015-01', 'r') as file:

    for i in range(9999):
        json_objects.append(json.loads(file.readline()))
        #print(file.readline())

print(json_objects)
for p in json_objects:
    print(p['subreddit'])

for f in *; do
    mv -- "$f" "${f%}.json"
done

suffix_list = []
for i in list(string.ascii_lowercase):
    for t in list(string.ascii_lowercase):
        suffix_list.append('%s%s' % (i, t))

print(suffix_list)
"""

suffix_list = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            suffix_list.append('%s%s%s' % (i, j, k))

print(len(suffix_list))