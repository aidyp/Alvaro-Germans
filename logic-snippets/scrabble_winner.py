import json

'''
I'm a bit sick of losing to Katie on words with friends. I'm not very good at scrabble so I'm gonna make my computer do it
'''

primify = {'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,
'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101}

scrabble_scores = {'a':1, 'e':1, 'i':1, 'o':1, 'l':1, 'n':1, 's':1, 't':1, 'r':1, 'd':2, 'g':2, 'b':3, 'c':3, 'm':3, 'p':3, 'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 'k':5, 'j':8, 'x':8, 'q':10, 'z':10}

def numberfy(word):
	out = 1
	for letter in word:
		out *= primify[letter]
	return out

def load_map():
	with open('../disk/scrabble_anagram_map.json') as fd:
		anagram_map = json.load(fd)
	return anagram_map


def find_words(letters_key, anagram_map):
	'''
	Given a list of words that has been primified, return the scrabble words you can make
	'''

	try:
		return anagram_map[str(letters_key)]
	except:
		return []

def pretty_print_by_length(possible_words):
	'''
	Words come in as a list, first element is the key, later elements are the words
	'''
	print("Words with length " + str(len(possible_words[1])) + ": ")
	set_words = set(possible_words[1:])
	for i in range(1, len(possible_words)):
		print possible_words[i]
	print("")

def pretty_print_by_score(words, score):
	'''
	Words come in as a list
	'''
	print("Words with score " + str(score) + ": ")
	for i in range(0, len(words)):
		print words[i]
	print("")

def sort_of_powerset(input_word):
	'''
	Create a powerset of all the possible words that could be formed,
	but strip out words of length 1
	'''
	s = list(input_word)
	x = len(s)
	powerset = []
	for i in range(1 << x):
		subset = [s[j] for j in range(x) if (i & (1 << j))]
		# Scrabble doesn't have any length zero or one words, so don't need these options
		if len(subset) > 1:
			powerset.append(subset)
	return powerset
	
def return_possible_words(word):
	ana_map = load_map()
	options = sort_of_powerset(word)
	s_words_by_len = {}
	for subset in options:
		key = numberfy(subset)
		scrabble_words = find_words(key, ana_map)
		if len(scrabble_words) > 1:
			len_word = len(scrabble_words[1])
			if not (len_word in s_words_by_len):
				s_words_by_len[len_word] = []
			s_words_by_len[len_word] += scrabble_words[1:]
	return s_words_by_len

def scrabble_score_word(word):
	score = 0
	for letter in word:
		score += scrabble_scores[letter]
	return score

def tableau_words_by_score(word_list):
	'''
	Given all of the words that one could play with the letters available, we want to return them indexed by score
	'''
	words_by_score = {}
	for word in word_list:
		word_score = scrabble_score_word(word)
		
		if word_score in words_by_score:
			words_by_score[word_score] += [word]
		else:
			words_by_score[word_score] = [word]
	
	return words_by_score

def unroll_dict(word_dict):
	'''
	Temporary function to get to a scrabble scoring, should re-factor this later!
	'''
	ret = []
	for key in word_dict:
		ret += word_dict[key]
	return ret



def process_input():
	
	x = raw_input("Enter your scrabble letters: ")
	out = return_possible_words(x)
	words = unroll_dict(out)
	scored_words = tableau_words_by_score(words)
	# sort the list of keys
	k_list = list(scored_words.keys())
	k_list.sort(reverse=True)

	# Print the results to console
	for key in k_list:
		pretty_print_by_score(scored_words[key], key)
	
process_input()


