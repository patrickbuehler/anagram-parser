# Patrick Buehler
# Duolingo Programming Task: Anagram parser
# 4 November 2016

import sys

def compare_strings(str1, str2):
	"""
	compare_strings takes two strings as arguments, trims leading and trailing
	whitespace, and returns a boolean True if they are anagrams of each other,
	FALSE otherwise.
	"""

	# sort the strings in lex order
	str1 = sorted(str1.strip())
	str2 = sorted(str2.strip())

	# can break early if they are not even the same length
	if len(str1) != len(str2):
		return False

	# otherwise, compare the ith character of each of the sorted strings.
	for char1, char2 in zip(str1,str2):
		if char1 != char2:
			return False

	return True

if __name__ == "__main__":
	while True:
		# get input
		print("Please enter two strings.")
		str1 = raw_input("First string: ")
		str2 = raw_input("Second string: ")
		if (compare_strings(str1,str2)):
			print("Yes! '{}' and '{}' are anagrams of one another.".format(str1.strip(),str2.strip())
			sys.exit()
		else:
			print("No :( these are not anagrams. Please try again.")
