#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


X = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [7.0, 3.2, 4.7, 1.4],
    [6.4, 3.2, 4.5, 1.5],
    [6.3, 3.3, 6.0, 2.5],
    [5.8, 2.7, 5.1, 1.9]
])

Y = np.array([
    [1.2, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

yeni_ornek = np.array([5, 3.4, 1.5, 0.2])


X_birlestirilmis = np.hstack((np.ones((X.shape[0], 1)), X))
coefficients = np.linalg.inv(X_birlestirilmis.T.dot(X_birlestirilmis)).dot(X_birlestirilmis.T).dot(Y)
print("Doğrusal Regresyon Katsayıları:")
print(coefficients)


yeni_ornek_birlestirilmis = np.hstack((1, yeni_ornek))
predicted_classes = yeni_ornek_birlestirilmis.dot(coefficients)
print("Yeni örneğin sınıf tahmini:")
print(predicted_classes)


# In[ ]:




