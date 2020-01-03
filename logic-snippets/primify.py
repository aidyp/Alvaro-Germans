#Anagram comparison primitives by observation of primes

primify = {}
primify['a'] = 2
primify['b'] = 3
primify['c'] = 5
primify['d'] = 7
primify['e'] = 11
primify['f'] = 13
primify['g'] = 17
primify['h'] = 19
primify['i'] = 23
primify['j'] = 29
primify['k'] = 31
primify['l'] = 37
primify['m'] = 41
primify['n'] = 43
primify['o'] = 47
primify['p'] = 53
primify['q'] = 59
primify['r'] = 61
primify['s'] = 67
primify['t'] = 71
primify['u'] = 73
primify['v'] = 79
primify['w'] = 83
primify['x'] = 89
primify['y'] = 97
primify['z'] = 101

def numberfy(word):
	out = []
	for letter in word:
		out.append(primify[letter])
	return out

result = numberfy("banana")
print(result, reduce(lambda x,y: x*y, result))
