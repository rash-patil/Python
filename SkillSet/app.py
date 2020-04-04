#!/usr/bin/python3

import os
import pandas as pd 
import numpy as np
import xlsxwriter
from xlsxwriter import Workbook
import sys
import time

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#sprint 'Argument List:', str(sys.argv)

Input=sys.argv
if len(sys.argv)<3:
	print("Input1=Folder_Path,Input2=Skill_Name")
	time.sleep(2)
	sys.exit()

path = os.getcwd()
files = os.listdir(Input[1])
#print(files)

files_xlsx= [f for f in files if f[-4:]=='xlsx']
#print(files_xlsx)

df = pd.DataFrame()

for f in files_xlsx:
    data = pd.read_excel(f)
    df = df.append(data)
#print(df)
writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
workbook=writer.book

df1 = pd.DataFrame(data=df)
df1.to_excel (writer,index = False)
writer.save()

writer2 = pd.ExcelWriter(str(Input[2])+'.xlsx', engine='xlsxwriter')

df2=pd.read_excel('dataframe.xlsx')
skillname=((df2['Unnamed: 19']== Input[2]) & (df2['Emp. Name']!=0))
a=df2.loc[skillname,['Unnamed: 19','Unnamed: 15','Unnamed: 14','Emp. Name']]

a.rename(columns={'Unnamed: 19': 'Skill_Name', 'Unnamed: 15': 'Emp. Name','Unnamed: 14': 'Emp. Id','Emp. Name': 'self_assessment',}, inplace=True)

print(a)

df3=pd.DataFrame(data=a)
df3.to_excel (writer2,index = False)
writer2.save()

os.remove('dataframe.xlsx')




