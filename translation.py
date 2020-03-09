
import dictionary

print(dictionary.d)

text = "I am Italian"
translate = ""
words = text.split()
for w in words:
    translate = translate + " " + dictionary.d[w]

print(translate)




