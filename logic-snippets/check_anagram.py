# This snippet is for finding out what the unscrambled word is #
# At the moment it can only handle single scrambled words #

import json

# primify global #
primify = {'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,
'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101}

def numberfy(word):
	out = 1
	for letter in word:
		out *= primify[letter]
	return out

def load_map():
	with open('../disk/anagram_map.json') as fd:
		anagram_map = json.load(fd)
	return anagram_map

def check_anagram(word, anagram_map):
	key = numberfy(word)
	try:
		return anagram_map[str(key)]
	except:
		return []

def check_anagram_word_recursive(key, anagram_map, size):
	# Idea is to solve it like the sudoku puzzle #
	# So far it returns the _first_ solution
	
	out = []
	# Limiting Condition #
	if size == 1:
		try:
			return anagram_map[str(key)]
		except:
			# This isn't going to work #
			return []
	
	for word_key in anagram_map:
		# Check if a word in the map is present in the target word #
		if key % int(word_key) == 0:			
			# Take head and tail of the key #
			head = int(word_key)
			h_word = anagram_map[word_key]			
			out.append(h_word)
			tail = key / head
			out.append(check_anagram_word_recursive(tail, anagram_map, size - 1))
			if len(out[-1]) == 0:
				# This is a failure, nothing was found #
				out = []
			else:
				# We can return the head
				return out
			
	
				
			

def check_anagram_words(word, anagram_map, size):	
	# Run when you have a guess of how many words an anagram resolves to #
	key = numberfy(word)
	pairs = []
	
	# First guess is when it's two words
	for word_key in anagram_map:
		# Check if a word in the map is present in the target word #
		if key % int(word_key) == 0:
			# Divide the key #
			left_key = key / int(word_key)
			right_key = int(word_key)
			try:
				# Check if the result is also a word #
				right_word = anagram_map[str(right_key)]
				left_word = anagram_map[str(left_key)]
				pairs.append((left_word[1:], right_word[1:]))
			except:
				pass
	
	
	# At the moment, it's doubling the list, should make sure a word isn't added more than once #
	# Also how do I tell the best candidates? #
	return pairs

def print_results(results):
	for elem in results:
		print(elem)

def main():
	anagram_map = load_map()
	word = 'alvarogerman'
	result = check_anagram_word_recursive(numberfy(word), anagram_map, 3)
	print_results(result)
	
main()

