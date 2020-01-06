def reversed_word(sequence):
	return ' '.join(word[::-1]for word in sequence.split())
str=input()
reversed_word(str)
print(reversed_word(str))
