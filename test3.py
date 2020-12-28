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
	for i in lines:				#or rach row
		for j in i.split(' '):		#for each word in a column that is seperated by whitespace
			words.append(j) 	
	#print(words)
	k=0
	for i in range(cols):
		
		m=k
		for p in range(rows):
			#print(words[m])
			arr.append(words[m])	#appends in such a way that the words are appended in column wise
			#print(words[m])
			m=m+cols

		k=k+1
		
	print(arr)
	val=input("enter the string : ")
	flag=0					#flag is to verify whether given input is in the word array or not
	for i in range(len(words)):
		if val==arr[i]:
			t=i
			flag=1  	#tells given word does exist in word array

	
	if flag==0:
		print("Given string doesnot exist")
	else :
		print(arr[t-rows])			#prints the coressponding value
if __name__== '__main__':
	main()
