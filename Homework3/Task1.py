with open("JEOPARDY_CSV.csv", 'rb') as f:
    head = f.readline().decode('utf8')
    print(head)
    for i in range(10):
        data = f.readline().decode('utf8')
        print (data)
    f.seek(0)
    for i in range(5):
        data = f.readline().decode('utf8')
        print (data)
         
    keys = head.split(',')
    for i,key in enumerate(keys) : keys[i]=str.strip(key)
    print(keys)

import re
from datetime import date

with open("JEOPARDY_CSV.csv", 'rb') as f:
    head = f.readline().decode('utf8')
    keys =  re.findall(r',?\s?([^,]+)(?:,|\r\n)', head)
    showsDict = {}
    for key in keys:
        showsDict.update({key:[]})
    for line in f:
        line = line.decode('utf8')
#        values = re.findall(r',?([^,\s]+)(?:,|\r\n)', line)
        values = re.split('''((?:[^,"']|"[^"]*"|'[^']*')+)''',line)[1::2]
        items = dict(zip(keys, values))
        items['Show Number'] = int(items['Show Number'])
        if re.search('none',items['Value'], re.IGNORECASE ):
            items['Value'] = 0;
        else:
            items['Value'] = re.findall('\d+',items['Value'])[0]
            items['Value'] = int(items['Value'])
        items['Answer'] = re.findall('([^\r\n]+)',items['Answer'])[0];
        items['Air Date'] = date.fromisoformat(items['Air Date'])
        for key in keys:
            showsDict[key].append(items[key])

import json
with open("Jeopardy.json","w+") as out:
    json.dump(showsDict, out, default=str)

import pickle
with open('jeopardy.pickle', 'wb') as f:
    pickle.dump(showsDict, f, pickle.HIGHEST_PROTOCOL)
