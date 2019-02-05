original = input('Enter a word:')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    if(first == ("a" or "e" or "i" or "o" or "u")):
     print("Vowel")
    else:
     print("Consonant")
else:
    print("invalid")
