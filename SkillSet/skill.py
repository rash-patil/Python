import pandas as pd
import numpy as np
#jhjjh
skill= pd.read_excel('Prash.xlsm')
#print(skill.columns)
#print(skill['Employee Skill Survey'])
name=['Employee name:',skill.columns[5]] #name
emp_ID=['Employee ID:',skill.iloc[0,5]] #employee id
emp_grade=['Employee Grade:',skill.iloc[0,10]] #Employee Grade
emp_role=['Employee Role:',skill.columns[10]]
#print(type(skill['Self Assessment']))
SA= skill['Emp. Name']==1
a=skill.loc[SA,['Unnamed: 3','Prashant B']]

SA2= skill['Emp. Name']==2
b=skill.loc[SA2,['Unnamed: 3','Prashant B']]

SA3= skill['Emp. Name']==3
c=skill.loc[SA3,['Unnamed: 3','Prashant B']]

beg=[]
beg.append(['begginer','l'])
beg=beg+a.values.tolist()
user=[]
user.append(['user','l'])
user=user+b.values.tolist()
expert=[]
expert.append(['expert','l'])

na=[]
na.append(name)
na.append(emp_ID)
na.append(emp_grade)
na.append(emp_role)


expert=expert+c.values.tolist()

exe= na+beg+user+expert

df = pd.DataFrame(data=exe, columns=['SKILL_NAME','specific'])

print(exe)
df.to_excel (r'export_dataframe.xlsx', index = False, header=True)

