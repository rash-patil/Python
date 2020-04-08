import pandas as pd 
import numpy as np
import xlsxwriter
from xlsxwriter import Workbook


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
#print('index',a)
SA2= skill['Emp. Name']==2
b=skill.loc[SA2,['Unnamed: 3','Prashant B']]

SA3= skill['Emp. Name']==3
c=skill.loc[SA3,['Unnamed: 3','Prashant B']]

beg=[]
beg.append(['Begginer','l'])
beg=beg+a.values.tolist()
user=[]
user.append(['User','l'])
user=user+b.values.tolist()
expert=[]
expert.append(['Expert','l'])
expert=expert+c.values.tolist()

na=[]
na.append(name)
na.append(emp_ID)
na.append(emp_grade)
na.append(emp_role)
#exe= na+beg+user+expert

writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
workbook=writer.book


df1 = pd.DataFrame(data=na)
df2 = pd.DataFrame(data=beg)
df3 = pd.DataFrame(data=user)
df4 = pd.DataFrame(data=expert)

df1.to_excel (writer,startrow = 0,sheet_name ='Sheet1', index = False, header=False)
df2.to_excel (writer,startrow = 5,sheet_name ='Sheet1', index = False, header=False)
df3.to_excel (writer,startrow = 20,sheet_name ='Sheet1', index = False, header=False)
df4.to_excel (writer,startrow = 35,sheet_name ='Sheet1', index = False, header=False)

format1= workbook.add_format({'bold': True,'italic' : True,'text_wrap': True, 'valign': 'top','font_color': 'red'})
format2= workbook.add_format({'valign': 'left'})

worksheet=writer.sheets['Sheet1']
worksheet.write('A6','Begginer',format1)
worksheet.write('A21','User',format1)
worksheet.write('A36','Expert',format1)

worksheet.set_column('B:B', None, format2)
writer.save()
