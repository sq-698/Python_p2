import collections
import q2

poem = ""
f = open("wasteland.txt", "r")
for x in f:
    poem = poem + x

words = (poem.lower().split())

poem_dic = q2.word_frequncy(words)

