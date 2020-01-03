import numpy as np
seed = 17  
np.random.seed(seed)  # установка генератора случайных чисел в фиксированное положение
a = list(np.random.randint(0, high=100, size=300)) + list(np.random.randint(0, high=25, size=300)) + list(np.random.randint(25, high=75, size=300)) + list(np.random.randint(0, high=200, size=1000)) + list(np.random.randint(0, high=10, size=1000)) + list(np.random.randint(50, high=60, size=10000))
a = np.array(a)
np.random.shuffle(a)
a = list(a)
#print(a)

keys = set(a)
#print(keys)
dict = {}
dict = {i: 0 for i in keys}
for i in a:
    dict[i] +=1
dict = {key : value for key, value in sorted(dict.items(), key = lambda kv: kv[1], reverse = True)}
for elements, counts in dict.items():
    print(elements, '->', counts)

