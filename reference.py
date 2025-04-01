import sys

from chaininghashtable import ChainingHashTable
from linearprobinghashtable import LinearProbingHashTable
from quadraticprobinghashtable import QuadraticProbingHashTable

# read words from input, one word per line
# then use a dictionary to count which word is most frequent
# but sometimes try to remove the word
# and then print the most frequent word and if there are multiple
# most frequent take the first one in alphabetical order

# d = { }

# i = 0

# for line in sys.stdin:
# 	word = line.strip()
# 	is_present = word in d
# 	remove_it = i % 16 == 0

# 	if is_present:
# 		if remove_it:
# 			del d[word]
# 		else:
# 			count = d[word]
# 			d[word] = count + 1
# 	elif not remove_it:
# 		d[word] = 1
# 	i += 1

# (count, word) = max(zip(d.values(), d.keys()))

# for k in d:
# 	if d[k] == count and k < word:
# 		word = k

# print(word, count)


d = QuadraticProbingHashTable(2**20, 0.35)

i = 0

for line in sys.stdin:
	word = line.strip()
	is_present = d.contains(word) # word in d
	remove_it = i % 16 == 0

	if is_present:
		if remove_it:
			d.remove(word) # del d[word]
		else:
			count = d.get(word) # d[word]
			d.insert(word, count + 1) # d[word] = count + 1
	elif not remove_it:
		d.insert(word, 1) # d[word] = 1
	i += 1

(count, word) = max(zip(d.get_values(), d.get_keys()))

keys = d.get_keys()

for key in keys:
	if d.get(key) == count and key < word:
		word = key

print(word, count)
