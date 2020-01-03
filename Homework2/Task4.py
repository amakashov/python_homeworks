import numpy as np
import matplotlib.pyplot as plt
seed = 29              
np.random.seed(seed)  # установка генератора случайных чисел в фиксированное положение
x = np.linspace(0, 10*np.pi, 1000)
signal = list(np.sin(x) + np.sin(x)**2 + 1 / np.sqrt((x + 1)) * np.sqrt(2 + np.sin(x))) + np.random.rand(1000)

def windowFilter(signal, window, padding = True):   #   По умолчанию будем дополнять
    if padding:                                     #   Итак, если дополняем, то
        halfWindow = (window-1) //2                 #   Расчитаем размер половины окна
        paddedSignal = signal[halfWindow:0:-1].tolist()     #   Сначала добавим отзеркаленую левую границу
        paddedSignal += signal[::].tolist()                 #   Потом сам массив
        paddedSignal += signal[-2:-halfWindow-2:-1].tolist()#   Потом отзеркаленную правую границу
        signal = paddedSignal
    filtSum = sum(signal[:window:])                 #       Считаем сумму первого окна в лоб
    data = [filtSum/window]                         #       И запихиваем её в выходной массив
    for i in range(1, len(signal)-window+1):        #       А потом по оставшимся элементам
        filtSum+=signal[i+window-1]-signal[i-1]     #       Считаем сумму как плюс новый элемент минус выпавший
        data.append(filtSum/window)                 #       И добавляем, добавляем
    return data

from matplotlib import pyplot as plt
out = windowFilter(signal, 15)                      #       Собственно, вызов
x = [i for i in range(len(signal))]
x1 = [i for i in range(len(out))]
plt.figure()
plt.plot(x,signal.tolist())          #  Тут, наверное, их надо было поаккуратнее совместить
plt.plot(x1,out)                     #  Но было лень
plt.show()


