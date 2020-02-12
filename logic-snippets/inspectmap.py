# This snippet is for inspecting the map to find out some useless facts #

import json

def load_map():
	with open('../disk/anagram_map.json') as fd:
		anagram_map = json.load(fd)
	return anagram_map

def find_anagrams(anagram_map):
	# Data entries > 1 are anagrams #

	for key in anagram_map:
		anagrams = anagram_map[key]
		if len(anagrams) > 1:
			print(anagrams)
	
	return 0

def find_most_anagrams(anagram_map):
	longest = ['dummy']
	for key in anagram_map:
		anagrams = anagram_map[key]
		if len(anagrams) > len(longest):
			longest = anagrams
	return longest

def main():
	anagram_map = load_map()
	longest = find_most_anagrams(anagram_map)
	print(longest)

main()
