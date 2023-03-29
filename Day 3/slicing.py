text = "ABCDEFGHIJKLM"
fragment = text[2]
print(fragment)

"Variations"
text = "ABCDEFGHIJKLM"
fragment = text[2:5]
print(fragment)


text = "ABCDEFGHIJK"
fragment = text[2:]
print(fragment)

text = "ABCDEFGHIJKLM"
fragment = text[:5]
print(fragment)

"skipping by 2"
text = "ABCDEFGHIJKLM"
fragment = text[2:10:2]
print(fragment)

text = "ABCDEFGHIJKLM"
fragment = text[::3]
print(fragment)

text = "ABCDEFGHIJKLM"
fragment = text[::-2]
print(fragment)

"practice: extract the first word of the sentence using slicing"
my_sentence = "Controlling complexity is the essence of programming"
fragment = my_sentence[0:11]
print(fragment)

"practice: Take every third character from the ninth to the end of the sentence and print the result"
my_sentence = "Never trust a computer you can't throw out a window"
fragment =my_sentence[8::3]
print(fragment)

"practice: reverse the position of all the characters in the sentence"
my_sentence = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
fragment = my_sentence[:: -1]
print(fragment)