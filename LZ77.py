import time 
import math
import sys

def find_prefix(text,right, buffer_window):
	longest_start = 0
	longest = 0
	if right-buffer_window<0:
		begin = 0
	else:
		begin = right-buffer_window
	for i in range(begin,right):
		highest=0
		for j in range(0,right-i):
			if right+j<len(text) and text[i+j]==text[right+j]:			
					highest = highest + 1
			else:
				break
		if longest<=highest and highest!=0:
			longest = highest
			longest_start = i
	return longest, (right-longest_start)


def encode(text, buffer_window, name):
	size=0
	code=[]
	y=0
	length_prefix=0
	loops=0
	while(y<len(text)+1):
		loops=loops+1
		length_prefix, start = find_prefix(text,y, buffer_window)		
		i=start
		l=length_prefix
		if y+length_prefix==len(text):
			c='-'
		elif length_prefix !=0:
			c=text[y+l]
		else:
			i=0
			l=0
			c=text[y]
		size = size + math.log(buffer_window+1,2)+math.log(buffer_window+1,2)+8
		code.append([i,l,c])
		y=y+(length_prefix+1)
	file_name = "encoded_"+name+"_"+str(buffer_window)
	with open(file_name, "w") as text_file:
		text_file.write(str(code))
	return(code)

def decode(code):
	text=[]
	for i in range(0, len(code)):
		if code[i][1]==0:
			text.append(code[i][2])		
		else:
			start=len(text)-code[i][0]
			for j in range(0,code[i][1]):
				text.append(text[start+j])
			text.append(code[i][2])

	return ''.join(text)

def main(buffer_window, file_name):
	with open(file_name) as file1:
		text=[]
		text.append(file1.read().replace('\n', ''))
	file1.close()
	encoded_data=[]
	decoded_data = []
	for j in range(0, len(text)):
		start=time.time()
		data = encode(text[j],buffer_window,file_name[j])
		stop = time.time()
		encoded_data.append(data)
		message= "\nBuffer window size = " + str(buffer_window) + "\n" + "Time taken for ENCODING "+ file_name[j]+ ": " + str(stop-start)
		print("Time taken for ENCODING", file_name[j], ": ", stop-start)

		with open("encoding.txt", "a") as text_file:
			text_file.write(message+'\n')

	for j in range(0, len(encoded_data)):
		start=time.time()
		data = decode(encoded_data[j])
		stop = time.time()
		decoded_data.append(data)
		message= "\nBuffer window size = " + str(buffer_window) + "\n" + "Time taken for DECODING "+ file_name[j]+ ": " + str(stop-start)
		print("Time taken for DECODING", file_name[j], ": ", stop-start)

		with open("decoding.txt", "a") as text_file:
			text_file.write(message+'\n')

if __name__ == "__main__":
    buffer_window = int(sys.argv[1])
    file_name = str(sys.argv[2])
    main(buffer_window, file_name)