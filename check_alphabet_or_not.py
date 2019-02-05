original = input('Enter a word:')
word = original.lower()
first = word[0]
if len(original) > 0 and original.isalpha():
 if(first == ("a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z")):
  print("Alphabet")
 else:
  print("")
else:
  print("No")
