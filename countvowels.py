def count_vowels_in_word(word):
	count = 0
	
	for char in word:
		if char.lower() in'aeiou':
		    count = count + 1
	return count


userinput = input("Enter a word:")
print(userinput)
print(count_vowels_in_word(userinput))
