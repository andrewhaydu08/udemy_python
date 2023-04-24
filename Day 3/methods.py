text = "We are going to learn six methods today"
result = text
print(result)

"uppercase"
text = "We are going to learn six methods today"
result = text.upper()
print(result)

# using a index
text = "We are going to learn six methods today"
result = text[4].upper()
print(result)

# lowercase
text = "We are going to learn six methods today"
result = text.lower()
print(result)

# split: it will spit the strings in several parts
text = "We are going to learn six methods today"
result = text.split()
print(result)

text = "We are are going to learn six methods today"
result = text.split("o")
print(result)

# join is the opposite of split
a = "learning"
b = "python"
c = "is"
d = "amazing"
e = " ".join([a, b, c, d])
print(e)
# another example with (-)
a = "learning"
b = "python"
c = "is"
d = "amazing"
e = "-".join([a, b, c, d])
print(e)

# find : this will find your letter or word
text = "We are going to learn six methods today"
result = text.find("s")
print(result)

text = "We are going to learn six methods today"
result = text.find("-1")
print(result)

# replace
text = "We are going to learn six methods today"
result = text.replace("six", "a lot of")
print(result)

# practice: print the following text in uppercase using the specific string method
my_sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
result = my_sentence.upper()
print(result)

# Join the following list into a string separating each item with a space. Use the appropriate list/string method and dissplay the result.
word_list = ["Simple", "is", "better", "than", "complex"]
a = "Simple"
b = "is"
c = "better"
d = "than"
e = "complex"
f = " ".join([a, b, c, d, e])
print(f)

word_list = ["Simple", "is", "better", "than", "complex"]
result = " ".join(word_list)
print(result)

# replace in the following sentence: If the implementation is hard to explain, it might be a bad idea.
# the following pair of words:
# 1 hard = easy
# bad = good
sentence = "If the implementation is hard to explain, it might be a bad idea."
print(sentence.replace("hard", "easy") .replace("bad", "good"))






