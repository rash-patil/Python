
# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog


from tkinter import messagebox as mb

import subprocess
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile
import os 
import app

root = Tk() 
root.title("Skill Set")
root.geometry('200x200') 


def browse_button():
	global filename
	filename = filedialog.askdirectory()


def RunButton():
	global filename
	app.MergeExcel(filename,SkillName.get())
	mb.showinfo('Done', 'Succesfully  Created File in file name '+str(SkillName.get())+'.xlsx')
	
#PathName.get()

#For the Type File
TypeText = Label(root,text="Folder Path ")
TypeText.pack()
TypeText.place(x=0,y=0)
TypeBrowse = Button(root, text ='Open', command = browse_button) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=110,y=0)



#For the Type File
TypeText = Label(root,text="Skill Name ")
TypeText.pack()
TypeText.place(x=0,y=30)
SkillName = Entry(root, width=10)
SkillName.pack(side = TOP, pady = 10) 
SkillName.place(x=110,y=30)




#Build/Run Button
Run = Button(root, text ="Run", command = RunButton)
Run.pack()
Run.place(x=110,y=160)

mainloop()
