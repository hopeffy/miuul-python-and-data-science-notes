#####################################################
# Pyhton ile veri analizi
######################################################

# - numpy : matematiksel işlemleri için
# - pandas : veri analizi ve manipülasyonları için (numpy üzerinde kuruludur.)
# - veri görselleştirme : matplotlib & seaborn
# - gelişmiş fonks. keşifçi veri analizi (Advanced functional exploratory data analysis)

######################################################
# NUMPY
######################################################

#####################################################
# neden numpy?
# hız : sabit tipte veri tutuyor.
# yüksek seviyede işlem yapmayı sağlar. vektör seviyesinde bir işlem
#####################################################

import numpy as np
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

######################################################
# numpy array
######################################################

import numpy as np

a = np.array([2, 3, 4, 5])
type(a)

np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))

######################################################
# numpy array özellikleri
######################################################

# ndim : boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi

a = np.random.randint(0, 10, size=5)
a.ndim
a.shape
a.size
a.dtype

######################################################
# reshaping
######################################################

# reshape yaparken size'a dikkat etmek gerekiyor.
ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)

######################################################
# index seçimi (index selection)
######################################################

b = np.random.randint(10, size=10)
b[0]
b[0:5]
b[0] = 999

# indexler 0dan başlayarak normal devam ediyor. ancak length gibi ögelerde sıfır yokmuş gibi.
c = np.random.randint(10, size=(3, 4))
c[0, 0]
c[1, 2] = 2.7

# numpy arrayleri tek tip array içerir.
c[:, 0]
c[1, : ]
c[0:2, 0:4]

######################################################
# fancy index
######################################################

v = np.arange(0, 30, 3)
v[1]
v[4]

catch = [0, 2, 3]
v[catch]

######################################################
# numpy koşullu işlemler
######################################################

v = np.arange(0, 6, 1)

# klasik döngü

ab = []

for i in v:
    if i < 3:
        ab.append(i)

# numpy versiyonu - true false değerine göre return edilebilir

v < 3

v[v > 3]

######################################################
# matematiksel işlemler
######################################################

v = np.arange(0, 6, 1)
v / 5
v = v ** 3
v - 1

np.substrac(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

######################################################
# nupmy ile iki bilinmeyenli denklem çözümü
######################################################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

m = np.array([[5, 1], [1, 3]])
n = np.array([12, 10])

np.linalg.solve(m, n)