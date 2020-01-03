s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

shift = 2;  # шифр сдвига - это же не надо было вычислять?

# Попытка №1 - в лоб через коды символов
s2 = ""
for symb in s:
    if (symb.isalpha()):    # если это буква
        code = ord(symb) + shift   # найдём код и сдвинем
        if (code > ord('z')):      # если больше z 
            code = code % (ord("z"))+ord("a")-1 #   вернём в исходный диапазон
        symb = chr(code)    # И вот тут бы надо ещё смотреть, а если сдвиг в минус
    s2+=symb
print(s2)

#   Поскольку решение кривое, то, в соответствии с рекомендацией
#   Попытка номер 2
input = [chr(i) for i in range (ord('a'), ord('z')+1)]  # Набор исходных букв
output = input[shift::]                                 # Набор букв со сдвигом
output += input[:shift:]                                # Что приятно - работает для сдвига в любую сторону

trans = str.maketrans(str(input), str(output))          # таблица перекодирования
s3 = str.translate(s, trans)                            # собственно перекодирование
print (s3)
