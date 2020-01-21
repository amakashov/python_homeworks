#Чтение заголовка и 5 строк
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

# Собственно, парсинг
import re
from datetime import date

with open("JEOPARDY_CSV.csv", 'rb') as f:
    head = f.readline().decode('utf8')
    keys =  re.findall(r',?\s?([^,]+)(?:,|\r\n)', head) # разобрали строку заголовков на ключи
    showsDict = {}
    for key in keys:
        showsDict.update({key:[]}) # словарь с пустыми листами
    for line in f:  
        line = line.decode('utf8')
#        values = re.findall(r',?([^,\s]+)(?:,|\r\n)', line)
        # Вот это шаманство - для того, чтобы не разделять строку по запятым, находящимся в кавычках
        # Но вот кавычки внутри однотипных кавычек разбираться так не должны
        values = re.split('''((?:[^,"']|"[^"]*"|'[^']*')+)''',line)[1::2]
        #   словарик
        items = dict(zip(keys, values))
        items['Show Number'] = int(items['Show Number'])
        # Оказывается, Value - это не обязательно число
        if re.search('none',items['Value'], re.IGNORECASE ):
            items['Value'] = 0;
        else:   
            items['Value'] = re.findall('\d+',items['Value'])[0]
            items['Value'] = int(items['Value'])
        items['Answer'] = re.findall('([^\r\n]+)',items['Answer'])[0]; # Я сломался и не придумал, как это сделать лучше
        items['Air Date'] = date.fromisoformat(items['Air Date'])
        for key in keys:
            showsDict[key].append(items[key])

# Если же принять пожелание использовать стандартные функции как руководство к действвию :)
import pandas as pd
import numpy as np

data = pd.read_csv("JEOPARDY_CSV.csv", header = 0)
# убираем лишние пробелы в заголовках
data.rename(columns=lambda x: x.strip(), inplace = True)
data['Show Number']=pd.to_numeric(data['Show Number'])
data['Air Date']=pd.to_datetime(data['Air Date'])
# сейчас в datetime есть ещё ненужное время (полночь)
data['Air Date']=data['Air Date'].dt.date  # оставляем только дату
# Опять решения лучше не придумал - сначала заменяем все варианты None
data['Value'].replace(to_replace=re.compile('none',re.IGNORECASE), value="$0", inplace=True)
# потом переводим в целое число, убирая лишние $ и ,
data['Value'] = data['Value'].replace(to_replace=r'[\$,]', value='', regex=True).astype(int)
# всё, конвертируем в словарь
showsDict = data.to_dict(orient='list');

import json
with open("Jeopardy.json","w+") as out:
    json.dump(showsDict, out, default=str, indent = 2)

import pickle
with open('jeopardy.pickle', 'wb') as f:
    pickle.dump(showsDict, f, pickle.HIGHEST_PROTOCOL)