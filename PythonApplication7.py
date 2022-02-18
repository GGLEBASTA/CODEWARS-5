def duplicate_count(text): #функция для подсчёта дубликатов без учёта регистра(встречаются более одного раза в строке)
    ss = text.lower() #регистр не учитываем
    ant = [] #список для символов,которые мы уже обработали
    k = 0 #счётчик дубликатов
    z = list(ss) #превращаем строку в массив
    for i in z: #перебор в массиве
        if i in ant:
            continue
        else:
            ant.append(i)
            n = z.count(i)
            if(n>1): #если встретился более одного раза
                k = k + 1
            continue
    return k


m = duplicate_count("F78my8rSsRfSgc4diROZTUpebMMxJDJPrKoG06XC1CWqhUsThq0GecQOfCoYCzikI8gipK1mHdoEkY5MLf53c7rNF")
print(m)