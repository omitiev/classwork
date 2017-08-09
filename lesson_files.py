# f = open(r"/home/oleksii/Documents/file_test.txt", "r+")
# print(type(f))
# print(f.read(1))
# f.close()
import string
import pprint


with open(r"/home/oleksii/Documents/hhgttg.txt", "r+") as f:
    content = f.read().lower()

with open(r"/home/oleksii/Documents/skip_words.txt", "r+") as f:
    skip_words = f.read().lower()



list_word = content.split()
print(len(list_word))
print(len(skip_words))
word_stats = {}
for word in list_word:
    word = word.strip(string.punctuation)
    if word:
        if word in word_stats:
            word_stats[word] += 1
        else:
            word_stats[word] = 1



pprint.pprint(word_stats)
sorted(word_stats, key=word_stats.get, reverse=True)
print("%s:\t%s" % (key, word_stats['key']))