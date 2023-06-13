#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
#A şıkkı hocam
data = {
    'PERSONEL': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'MAAS': ['NORMAL', 'YÜKSEK', 'DÜŞÜK', 'YÜKSEK', 'DÜŞÜK', 'YÜKSEK', 'DÜŞÜK', 'YÜKSEK', 'DÜŞÜK', 'YÜKSEK', 'DÜŞÜK'],
    'DENEYİM': ['ORTA', 'YOK', 'YOK', 'ORTA', 'ORTA', 'İYİ', 'İYİ', 'ORTA', 'ORTA', 'İYİ', 'ORTA'],
    'GÖREV': ['UZMAN', 'UZMAN', 'YÖNETİCİ', 'YÖNETİCİ', 'YÖNETİCİ', 'YÖNETİCİ', 'YÖNETİCİ', 'UZMAN', 'UZMAN', 'UZMAN', 'UZMAN'],
    'MEMNUN': ['EVET', 'EVET', 'EVET', 'EVET', 'EVET', 'EVET', 'EVET', 'HAYIR', 'HAYIR', 'HAYIR', 'HAYIR']
}

df = pd.DataFrame(data)

print(df)


# In[5]:


import pandas as pd
#B şıkkı hocam
data = {
    'Sütun 1': ['BÖLÜNME', '1', '2', '3', '4', '5', '6', '7', '8'],
    'Sütun 2': ['SOL', 'MAAŞ = NORMAL', 'MAAŞ = YÜKSEK', 'MAAŞ = DÜŞÜK', 'DENEYİM = YOK', 'DENEYİM = ORTA', 'DENEYİM = İYİ', 'GÖREV = UZMAN', 'GÖREV = YÖNETİCİ'],
    'Sütun 3': ['SAĞ', 'MAAŞ={DÜŞÜK, YÜKSEK}', 'MAAŞ={DÜŞÜK, NORMAL}', 'MAAŞ={NORMAL, YÜKSEK}', 'DENEYİM={ORTA, İYİ}', 'DENEYİM={YOK, İYİ}', 'DENEYİM={YOK, ORTA}', 'GÖREV = YÖNETİCİ', 'GÖREV = UZMAN']
}

df = pd.DataFrame(data)

sol_sayilar = []
sag_sayilar = []

for i in range(1, 9):
    if 'NORMAL' in df.iloc[i, 1]:
        sol_sayilar.append(df.iloc[i, 2].count(','))  # Düşük ve yüksek örneklerin sayısını bulma
    else:
        sol_sayilar.append(0)

for i in range(1, 9):
    if 'DÜŞÜK' in df.iloc[i, 2] or 'YÜKSEK' in df.iloc[i, 2]:
        sag_sayilar.append(df.iloc[i, 1].count('='))  # Normal, düşük ve yüksek örneklerin sayısını bulma
    else:
        sag_sayilar.append(0)

sonuc_data = {
    'Sol Tarafta Örnek Sayısı': sol_sayilar,
    'Sağ Tarafta Örnek Sayısı': sag_sayilar
}

sonuc_df = pd.DataFrame(sonuc_data)

print(sonuc_df)


# In[12]:


import pandas as pd

#C şıkkı hocam
data = {
    'Sütun 1': ['BÖLÜNME', '1', '2', '3', '4', '5', '6', '7', '8'],
    'Sütun 2': ['SOL', 'MAAŞ = NORMAL', 'MAAŞ = YÜKSEK', 'MAAŞ = DÜŞÜK', 'DENEYİM = YOK', 'DENEYİM = ORTA', 'DENEYİM = İYİ', 'GÖREV = UZMAN', 'GÖREV = YÖNETİCİ'],
    'Sütun 3': ['SAĞ', 'MAAŞ={DÜŞÜK, YÜKSEK}', 'MAAŞ={DÜŞÜK, NORMAL}', 'MAAŞ={NORMAL, YÜKSEK}', 'DENEYİM={ORTA, İYİ}', 'DENEYİM={YOK, İYİ}', 'DENEYİM={YOK, ORTA}', 'GÖREV = YÖNETİCİ', 'GÖREV = UZMAN']
}

df = pd.DataFrame(data)


matris = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0.1, 0.2, 0.15, 0, 0, 0, 0.3, 0.25],
    [0, 0.05, 0, 0, 0.15, 0.4, 0.4, 0, 0],
    [0, 0.1, 0.2, 0.15, 0, 0, 0, 0.3, 0.25],
    [0, 0, 0.25, 0.1, 0.35, 0, 0, 0.3, 0],
    [0, 0, 0.25, 0, 0.15, 0.4, 0.4, 0, 0],
    [0, 0, 0.25, 0.1, 0, 0, 0, 0.6, 0.15],
    [0, 0, 0, 0.1, 0, 0, 0, 0.7, 0.2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1]
]


sol_olasiliklar = []
for i in range(1, 9):
    sol_olasiliklar.append(matris[i][0] / sum(matris[i]))


sag_olasiliklar = []
for i in range(1, 9):
    sag_olasiliklar.append(matris[i][0



# In[15]:


def calculate_twowing(df, column1, column2):
    total_samples = df.shape[0]
    column1_values = df[column1].unique()
    column2_values = df[column2].unique()
#d şıkkı hocam
    twowing_value = 0
    for value1 in column1_values:
        for value2 in column2_values:
            p11 = len(df[(df[column1] == value1) & (df[column2] == value2)]) / total_samples
            p10 = len(df[(df[column1] == value1) & (df[column2] != value2)]) / total_samples
            p01 = len(df[(df[column1] != value1) & (df[column2] == value2)]) / total_samples
            p00 = len(df[(df[column1] != value1) & (df[column2] != value2)]) / total_samples

            twowing_value += abs(p11 * (p10 - p01))

    return twowing_value

twowing_value = calculate_twowing(df, 'Sütun 1', 'Sütun 2')
print("Sütun 1 ve Sütun 2 için Twoing uygunluk değeri:", twowing_value)


# In[ ]:




