#!/usr/bin/env python
# coding: utf-8

# In[24]:


#SORU
import pandas as pd
import numpy as np

# Veriler
ages = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 16
c2 = 22

# Tabloyu oluşturmak için gerekliler
iterasyonlar = []
distance1 = []
distance2 = []
kumeyeAit = []
yeniC1 = [c1]
yeniC2 = [c2]
dataframes = []

for iterasyon in range(4):
    if iterasyon == 0:
        iterasyonlar.append(iterasyon + 1)
        distance1.append([abs(age - c1) for age in ages])
        distance2.append([abs(age - c2) for age in ages])
    else:
        distance1_iter = [abs(age - yeniC1[iterasyon-1]) if kume == 'c1' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance2_iter = [abs(age - yeniC2[iterasyon-1]) if kume == 'c2' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance1.append(distance1_iter + [0] * (len(ages) - len(distance1_iter)))
        distance2.append(distance2_iter + [0] * (len(ages) - len(distance2_iter)))

    kumeyeAit.append(['c1' if dist1 < dist2 else 'c2' for dist1, dist2 in zip(distance1[iterasyon], distance2[iterasyon])])

    yeniC1.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c1']) if 'c1' in kumeyeAit[iterasyon] else yeniC1[iterasyon])
    yeniC2.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c2']) if 'c2' in kumeyeAit[iterasyon] else yeniC2[iterasyon])

# Dataframe oluşturma
data = {
    'Örnekler': ages,
    'c1': [c1] * len(ages),
    'c2': [c2] * len(ages),
    'Distance1': distance1[-1],
    'Distance2': distance2[-1],
    'Kümeye Ait': kumeyeAit[-1],
    'Yeni c1': yeniC1[-1],
    'Yeni c2': yeniC2[-1]
}

df = pd.DataFrame(data)
dataframes.append(df)

# Tabloları yazdırma
for i, df in enumerate(dataframes):
    print(f"Iterasyon {i+1}:")
    print(df)
    print()


# In[ ]:


#Iteration 1:
import pandas as pd
import numpy as np


ages = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 15.33
c2 = 36.25


iterasyonlar = []
distance1 = []
distance2 = []
kumeyeAit = []
yeniC1 = [c1]
yeniC2 = [c2]
dataframes = []

for iterasyon in range(4):
    if iterasyon == 0:
        iterasyonlar.append(iterasyon + 1)
        distance1.append([abs(age - c1) for age in ages])
        distance2.append([abs(age - c2) for age in ages])
    else:
        distance1_iter = [abs(age - yeniC1[iterasyon-1]) if kume == 'c1' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance2_iter = [abs(age - yeniC2[iterasyon-1]) if kume == 'c2' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance1.append(distance1_iter + [0] * (len(ages) - len(distance1_iter)))
        distance2.append(distance2_iter + [0] * (len(ages) - len(distance2_iter)))

    kumeyeAit.append(['c1' if dist1 < dist2 else 'c2' for dist1, dist2 in zip(distance1[iterasyon], distance2[iterasyon])])

    yeniC1.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c1']) if 'c1' in kumeyeAit[iterasyon] else yeniC1[iterasyon])
    yeniC2.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c2']) if 'c2' in kumeyeAit[iterasyon] else yeniC2[iterasyon])


data = {
    'Örnekler': ages,
    'c1': [c1] * len(ages),
    'c2': [c2] * len(ages),
    'Distance1': distance1[-1],
    'Distance2': distance2[-1],
    'Kümeye Ait': kumeyeAit[-1],
    'Yeni c1': yeniC1[-1],
    'Yeni c2': yeniC2[-1]
}

df = pd.DataFrame(data)
dataframes.append(df)

for i, df in enumerate(dataframes):
    print(f"Iterasyon {i+1}:")
    print(df)
    print()


# In[ ]:


#Iteration 2:
import pandas as pd
import numpy as np


ages = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 18.56
c2 = 45.90


iterasyonlar = []
distance1 = []
distance2 = []
kumeyeAit = []
yeniC1 = [c1]
yeniC2 = [c2]
dataframes = []

for iterasyon in range(4):
    if iterasyon == 0:
        iterasyonlar.append(iterasyon + 1)
        distance1.append([abs(age - c1) for age in ages])
        distance2.append([abs(age - c2) for age in ages])
    else:
        distance1_iter = [abs(age - yeniC1[iterasyon-1]) if kume == 'c1' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance2_iter = [abs(age - yeniC2[iterasyon-1]) if kume == 'c2' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance1.append(distance1_iter + [0] * (len(ages) - len(distance1_iter)))
        distance2.append(distance2_iter + [0] * (len(ages) - len(distance2_iter)))

    kumeyeAit.append(['c1' if dist1 < dist2 else 'c2' for dist1, dist2 in zip(distance1[iterasyon], distance2[iterasyon])])

    yeniC1.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c1']) if 'c1' in kumeyeAit[iterasyon] else yeniC1[iterasyon])
    yeniC2.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c2']) if 'c2' in kumeyeAit[iterasyon] else yeniC2[iterasyon])


data = {
    'Örnekler': ages,
    'c1': [c1] * len(ages),
    'c2': [c2] * len(ages),
    'Distance1': distance1[-1],
    'Distance2': distance2[-1],
    'Kümeye Ait': kumeyeAit[-1],
    'Yeni c1': yeniC1[-1],
    'Yeni c2': yeniC2[-1]
}

df = pd.DataFrame(data)
dataframes.append(df)

for i, df in enumerate(dataframes):
    print(f"Iterasyon {i+1}:")
    print(df)
    print()


# In[ ]:


#Iteration 3:
import pandas as pd
import numpy as np


ages = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 19.50
c2 = 47.89


iterasyonlar = []
distance1 = []
distance2 = []
kumeyeAit = []
yeniC1 = [c1]
yeniC2 = [c2]
dataframes = []

for iterasyon in range(4):
    if iterasyon == 0:
        iterasyonlar.append(iterasyon + 1)
        distance1.append([abs(age - c1) for age in ages])
        distance2.append([abs(age - c2) for age in ages])
    else:
        distance1_iter = [abs(age - yeniC1[iterasyon-1]) if kume == 'c1' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance2_iter = [abs(age - yeniC2[iterasyon-1]) if kume == 'c2' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance1.append(distance1_iter + [0] * (len(ages) - len(distance1_iter)))
        distance2.append(distance2_iter + [0] * (len(ages) - len(distance2_iter)))

    kumeyeAit.append(['c1' if dist1 < dist2 else 'c2' for dist1, dist2 in zip(distance1[iterasyon], distance2[iterasyon])])

    yeniC1.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c1']) if 'c1' in kumeyeAit[iterasyon] else yeniC1[iterasyon])
    yeniC2.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c2']) if 'c2' in kumeyeAit[iterasyon] else yeniC2[iterasyon])


data = {
    'Örnekler': ages,
    'c1': [c1] * len(ages),
    'c2': [c2] * len(ages),
    'Distance1': distance1[-1],
    'Distance2': distance2[-1],
    'Kümeye Ait': kumeyeAit[-1],
    'Yeni c1': yeniC1[-1],
    'Yeni c2': yeniC2[-1]
}

df = pd.DataFrame(data)
dataframes.append(df)

for i, df in enumerate(dataframes):
    print(f"Iterasyon {i+1}:")
    print(df)
    print()


# In[ ]:


#Iteration 4:
import pandas as pd
import numpy as np


ages = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 19.50
c2 = 47.89


iterasyonlar = []
distance1 = []
distance2 = []
kumeyeAit = []
yeniC1 = [c1]
yeniC2 = [c2]
dataframes = []

for iterasyon in range(4):
    if iterasyon == 0:
        iterasyonlar.append(iterasyon + 1)
        distance1.append([abs(age - c1) for age in ages])
        distance2.append([abs(age - c2) for age in ages])
    else:
        distance1_iter = [abs(age - yeniC1[iterasyon-1]) if kume == 'c1' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance2_iter = [abs(age - yeniC2[iterasyon-1]) if kume == 'c2' else 0 for age, kume in zip(ages, kumeyeAit[iterasyon-1])]
        distance1.append(distance1_iter + [0] * (len(ages) - len(distance1_iter)))
        distance2.append(distance2_iter + [0] * (len(ages) - len(distance2_iter)))

    kumeyeAit.append(['c1' if dist1 < dist2 else 'c2' for dist1, dist2 in zip(distance1[iterasyon], distance2[iterasyon])])

    yeniC1.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c1']) if 'c1' in kumeyeAit[iterasyon] else yeniC1[iterasyon])
    yeniC2.append(np.mean([age for age, kume in zip(ages, kumeyeAit[iterasyon]) if kume == 'c2']) if 'c2' in kumeyeAit[iterasyon] else yeniC2[iterasyon])


data = {
    'Örnekler': ages,
    'c1': [c1] * len(ages),
    'c2': [c2] * len(ages),
    'Distance1': distance1[-1],
    'Distance2': distance2[-1],
    'Kümeye Ait': kumeyeAit[-1],
    'Yeni c1': yeniC1[-1],
    'Yeni c2': yeniC2[-1]
}

df = pd.DataFrame(data)
dataframes.append(df)

for i, df in enumerate(dataframes):
    print(f"Iterasyon {i+1}:")
    print(df)
    print()

