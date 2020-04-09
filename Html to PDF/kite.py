import os
#import requests
from shutil import copyfile
#import mechanicalsoup
from bs4 import BeautifulSoup
#import re
import pdfkit 

def ConverttoPDF(InputPath):
	cwd = os.getcwd()
	path= InputPath
	f=open(path, "r")

	head_tail = os.path.split(path)

	os.chdir(head_tail[0])
	html=f.read()
	#print(html)


	soup = BeautifulSoup(html, "lxml")
	#print(soup.prettify())
	for a in soup.find_all('a', href=True):
    		if '.html' in a['href']: 
    			Detail_URL=a['href']
	#print(Detail_URL)
	absolutepath=os.path.abspath(Detail_URL)

	head_tail = os.path.split(Detail_URL)
	path1=head_tail[0]+"/Segments"
	segment_file = [f for f in os.listdir(path1) if f.endswith('.html')] 
	#print(segment_file)

	copyfile(path1+'/'+segment_file[0], cwd+'/segmentcopy.html')

	os.chdir(cwd)
	try:
		pdfkit.from_file('segmentcopy.html', 'DetailPDF.pdf')
	except:
		print("Image path not found")
	os.remove('segmentcopy.html')

	#f1=open(Detail_URL, "r")
	#html=f1.read()
	#print(html)

#ConverttoPDF('/home/rashmi/Brainstorm/Programming/Python/Python/beautifulsoap/HTMLReport/ExecutionReport_08_04_20_17_40/Demo Test Pack_Iteration_1/HTMLReport/HTMLReport.html')






