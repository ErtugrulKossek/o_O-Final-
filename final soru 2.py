#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

degerler = ['<=30', '<=30', '31...40', '>40', '>40', '>40', '31...40', '<=30', '<=30', '>40', '<=30', '31...40', '31...40', '>40']
income = ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium']
student = ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no']
credit_rating = ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent']
comp = ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

tablo = pd.DataFrame(columns=['Yaş', 'Income', 'Student', 'Credit Rating', 'Comp'])

tablo['Yaş'] = degerler
tablo['Income'] = income
tablo['Student'] = student
tablo['Credit Rating'] = credit_rating
tablo['Comp'] = comp

print(tablo)



# In[7]:


P_yes = 9 / 14  
P_no = 5 / 14

P_age_yes = 2 / 9  
P_age_no = 3 / 5  

P_income_yes = 4 / 9  
P_income_no = 2 / 5  

P_student_yes = 6 / 9 
P_student_no = 1 / 5 

P_credit_yes = 6 / 9  
P_credit_no = 2 / 5  

P_X_yes = P_age_yes * P_income_yes * P_student_yes * P_credit_yes  
P_X_no = P_age_no * P_income_no * P_student_no * P_credit_no  

P_X_C_yes = P_X_yes * P_yes  
P_X_C_no = P_X_no * P_no  

if P_X_C_yes > P_X_C_no:
    print("Kişi bilgisayar alabilir.")
else:
    print("Kişi bilgisayar alamaz.")


# In[ ]:




