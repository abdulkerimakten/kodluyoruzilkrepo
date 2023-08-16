# 1.SORU : Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
#Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

#Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

"""
### 1. SORUNUN CEVABI
def flatten(x:list):
    new = list()
    for i in x:
        if type(i) != list:
            new.append(i)
        else:
            new.extend(flatten(i))
    return new

            
l1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(l1))
"""


# 2.SORU : Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

"""
### 2. SORUNUN CEVABI
def rev(x:list):
    new = list()
    for i in x:
        if type(i) != list:
            new.append(i)
        else:
            new.append(rev(i))
    new.reverse()
    return new

l2 = [[1, 2], [3, 4], [5, 6, 7]]
print(rev(l2))
"""