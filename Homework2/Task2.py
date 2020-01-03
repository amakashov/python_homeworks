import numpy as np
seed = 19              
np.random.seed(seed)  # установка генератора случайных чисел в фиксированное положение
ids = list(np.random.choice(range(1000), size=7, replace=False))    # id
names = ['ALEXANDRA__', 'EKaterINA', 'vladimir!!! FON Baron', '~_petr_~', '===s!!tanislav', 'alena+++', 'mik123hail']  
surnames = ['I_vANOva0009-sTrizhevskaya!!', '', '!Petrov',  'gluhih', 'Bolshih', '', 'Kutuzov']    
salaries = list(np.random.choice(range(10000, 100000), size=7, replace=True) / 19)

sorted_by_salary = True

import re
spec = {'_', '!', '=', '+', '~' }
for i in range (10):
    spec.add(str(i))
print(spec)

for i, name in enumerate(names):
    for symb in spec:
        name = name.replace(symb,'')
    name = name.capitalize()
    if (name=='') :
        name = "UNKNOWN"
    names[i] = name

for i, surname in enumerate(surnames):
    for symb in spec:
        surname = surname.replace(symb,'')
    sparts = surname.split('-')
    sparts = [part.capitalize() for part in sparts]
    surname = str('-').join(sparts)
    if (surname=='') :
        surname = "UNKNOWN"
    surnames[i] = surname

ids = [str(id) for id in ids]
s_ids = ','
print(s_ids.join(ids))

staff = {}
for i, id in enumerate(ids):
    person = {"name" : names[i], "surname":surnames[i], "salary":salaries[i]}
    staff.update({id:person})

sorted_staff = {id:value for id,value in sorted(staff.items(), key = lambda item : item[1]["salary"], reverse=True)}
if (sorted_by_salary):
    staff = sorted_staff

print('{}{}{}'.format("|", "="*(7+25+30+10+3),"|")) 
print('|{:>7}|{:^25}|{:^30}|{:>10}|'.format("id", 'Name', 'Surname', 'Salary'))
print('{}{}{}'.format("|", "="*(7+25+30+10+3),"|")) 

for id,element in staff.items():
    print('|{:>7}|{:^25}|{:^30}|{:>10.2f}|'.format(id, element['name'], element['surname'], element['salary']))
print('{}{}{}'.format("|", "="*(7+25+30+10+3),"|")) 
