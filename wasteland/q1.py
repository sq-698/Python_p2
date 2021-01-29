import collections
poem = ""
f = open("wasteland.txt", "r")
for x in f:
    poem = poem + x

#print(poem)

words = (poem.split())
n_words = len(words)
print(n_words)

uniq_words = set(words)
n_uniq_word = len(uniq_words)
print(n_uniq_word)

f = open("out_words_count.txt", "w")
f.write(str(n_words))
f.write("\n")
f.writelines(str(n_uniq_word))
f.close()
