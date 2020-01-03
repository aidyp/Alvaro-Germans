# This makes the (probably) JSON map between a primified word and what it should be


# required modules #
import json 

# primify global #
primify = {'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,
'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101}

def numberfy(word):
	out = 1
	for letter in word:
		out *= primify[letter]
	return out

def load_words():
	word_list = [line.rstrip('\n') for line in open('../disk/dictionary.txt')]
	return word_list

def make_map(word_list):
	anagram_map = {}

	for word in word_list:
		# Compute the key #
		key = numberfy(word)
		
		if key in anagram_map:
			# Word is an anagram of another word in the dictionary #
			(anagram_map[key]).append(word)
		else:
			anagram_map[key] = [word]
	
	return anagram_map

def write_map(anagram_map):
	# Write to disk as a JSON #
	with open('../disk/anagram_map.json', 'w') as fd:
		json.dump(anagram_map, fd)
	
	return 0

def main():
	words = load_words()
	anagrams = make_map(words)
	success = write_map(anagrams)
	assert success == 0

main()
