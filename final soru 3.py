#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
#A şıkkı

x = [1, 2, 2, 3, 4, 5, 6, 8, 10, 11,]
y = [3, 5, 3, 9, 7, 2, 8, 6, 6, 1, ]
z = ['Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Negatif',]


tablo = pd.DataFrame({'x': x, 'y': y, 'z': z})


print(tablo)


# In[4]:


import pandas as pd
import math
#B şıkkı
x = [1, 2, 2, 3, 4, 5, 6, 8, 10, 11]
y = [3, 5, 3, 9, 7, 2, 8, 6, 6, 1]
z = ['Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Negatif']

tablo = pd.DataFrame({'X': x, 'Y': y, 'Etiket': z})

X_new = 7
Y_new = 3


tablo['Oklid_Mesafesi'] = tablo.apply(lambda row: math.sqrt((row['X'] - X_new) ** 2 + (row['Y'] - Y_new) ** 2), axis=1)


tablo['Yakinlik_Sirasi'] = tablo['Oklid_Mesafesi'].rank()

print(tablo)


# In[6]:


en_yakin_komsular = tablo.nsmallest(3, 'Oklid_Mesafesi')
siniflar = en_yakin_komsular['Etiket'].value_counts()
yeni_ornek_sinif = siniflar.idxmax()

print("Yeni örnek sınıfı:", yeni_ornek_sinif)
#c şıkkı 


# In[ ]:




