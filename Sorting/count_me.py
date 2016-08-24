import re
import string

def count_me():
	'''
	>>> count_me()
	set 1
	move 2
	listoverride 1
	its 2
	previous 1
	content 1
	interesting 1
	listtable 1
	tuples 8
	main 1
	immutable 1
	python 4
	pocket 1
	cannot 1
	they 3
	fnil 2
	decimal 1
	dig 1
	list 1
	store 1
	contain 1
	talked 1
	directly 1
	series 2
	understood 1
	listlevel 1
	are 5
	tutorial 1
	even 1
	refresher 1
	what 1
	for 1
	brackets 1
	access 1
	written 1
	except 1
	here 1
	objects 2
	let 1
	key 1
	offset 1
	article 1
	change 1
	about 3
	parentheses 1
	ahead 1
	items 1
	fswiss 1
	journey 1
	colortbl 1
	today 1
	navigation 1
	top 1
	simple 1
	continuation 1
	levelmarker 1
	because 1
	references 1
	learning 1
	your 2
	size 1
	guess 1
	from 1
	create 1
	strings 1
	three 1
	opposed 1
	way 1
	forward 1
	type 1
	leveltext 1
	pard 5
	deeper 1
	that 3
	listhybrid 1
	differences 1
	lists 3
	copy 1
	levelnumbers 1
	than 1
	listname 1
	language 1
	consist 1
	this 3
	will 4
	can 3
	concepts 2
	grasp 2
	accessed 2
	similar 1
	and 4
	refreshers 1
	ordered 1
	links 1
	thus 1
	listtext 2
	topic 1
	talking 1
	have 1
	ready 1
	arialmt 1
	any 1
	dictionaries 2
	etc 1
	rather 1
	make 1
	tuple 2
	note 1
	very 1
	need 1
	square 1
	which 2
	you 8
	unless 1
	index 1
	ansi 1
	important 3
	two 2
	fonttbl 1
	helveticaneue 1
	monaco 1
	the 5
	order 1
	once 1
	'''

	freq = {} # To store the word and its corresponding word count
	file_obj = open('count.txt', 'r')
	word_content = file_obj.read().lower() # Turn all the words in our document into lowercase.

	reg_exp = re.findall(r'\b[a-z]{3,15}\b', word_content)

	for word in reg_exp:
		count = freq.get(word, 0) # Count the frequency for a word present in our document.
		freq[word] = count + 1 # Increase the count for each word occurring more than once

	freq_list = freq.keys()

	for word in freq_list:
		print word, freq[word]


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
