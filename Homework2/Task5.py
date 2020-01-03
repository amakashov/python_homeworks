# Третья необязательная задача

def palindromChecker(strings):
    ret = {}
    for mstr in strings:
        tmpstr = ""
        for symb in mstr:
            if symb.isalpha():
                tmpstr+=symb
        tmpstr=tmpstr.lower()
        newstr=tmpstr[::-1]
        isPali = (newstr==tmpstr)
        ret.update({mstr:isPali})
    return ret

strList = ['d', 'kazak', 'dobro', "Madam I'm Adam", "Some men interpret nine memos"]
paliList = palindromChecker(strList)
print(paliList)
