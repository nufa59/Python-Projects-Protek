import random
def shuffleString(x, n):
	result = []
	for i in range(n):
		acak = ''.join(random.sample(x, len(x)))
		result.append(acak)
	result = list(set(result))
	return result

print(shuffleString('aku', 3))