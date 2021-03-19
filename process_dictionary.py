from ic_attack import *

def is_english(mystr):
	for i in mystr:
		if ord(i) < 97 or ord(i) > 122: 
			return False
	return True

test2_dict = []
with open("english_dict.txt") as file:
    for line in file:
    	line = line.strip('\n')
    	if is_english(line):
    		test2_dict.append(line)

with open("english_dict_process.txt", "w") as f:
	for line in test2_dict:
		line += '\n'
		f.write(line)
