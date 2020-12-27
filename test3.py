import pytesseract
import numpy as np
from PIL import Image   #help for extra processing
def extract_text():

	img=Image.open('cap.png')
	output = pytesseract.image_to_string(img)      
	with open('harsha.txt',mode='w')as file:   #writes into new file
		file.write(output)	
	return output.strip()   #removes leading and trailing spaces
words=[]
def main():
	#rows, cols = (5, 3)
	text=extract_text()
	lines=text.split('\n')  		#returns a list of strings after breaking the given string by the specified separator.
	rows=len(lines)					#returns no of rows
	cols=len(lines[0].split(' '))		#returns number of columns
	arr=[]
	for i in lines:
		for j in i.split(' '):
			words.append(j) 	
	#print(words)
	k=0
	for i in range(3):
		
		m=k
		for p in range(5):
			#print(words[m])
			arr.append(words[m])
			#print(words[m])
			m=m+3

		k=k+1
		
	print(arr)
	val=input("enter the string : ")
	flag=0
	for i in range(len(words)):
		if val==arr[i]:
			t=i
			flag=1

	
	if flag==0:
		print("Given string doesnot exist")
	else :
		print(arr[t-rows])			#prints the coressponding value
if __name__== '__main__':
	main()
