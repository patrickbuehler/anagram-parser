# Patrick Buehler
# Duolingo Programming Task: Anagram parser
# 4 November 2016

import sys

def compare_strings(str1, str2):
	str1 = sorted(str1)
	str2 = sorted(str2)
	if len(str1) != len(str2):
		return False
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
		if (compare_anagrams(str1,str2)):
			print("Yes! '{}' and '{}' are anagrams of one another.".format(str1,str2))
			sys.exit()
		else:
			print("No :( these are not anagrams. Please try again.")
