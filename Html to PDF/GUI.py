
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
import kite

root = Tk() 
root.title("HTML TO PDF")
root.geometry('200x200') 


def RunButton():
	global HTML
	kite.ConverttoPDF(HTML)
	mb.showinfo('Done', 'Succesfully  Created File in file name DetailPDF.pdf')

def HTMLFile():
	global HTML
	file = askopenfile(mode ='r', filetypes =[('Select the HTML', '*.html')]) 
	HTML=file.name	
#PathName.get()



TypeText = Label(root,text="HTML TO PDF ")
TypeText.pack()
TypeText.place(x=0,y=0)
TypeBrowse = Button(root, text ='Open', command = lambda:HTMLFile()) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=110,y=0)

#Build/Run Button
Run = Button(root, text ="Run", command = RunButton)
Run.pack()
Run.place(x=110,y=160)

mainloop()
