__author__ = 'prakhardogra'

import csv
import ef

from stop_words import get_stop_words

stop_words = get_stop_words('en')

feature_set = []
class_set = []
f = open("labeled_tweets.csv","r")
text = csv.reader(f)
count = 0
for row in text:
    count += 1
    words = row[0].split(" ")
    word_list = []
    for word in words:
        if word in stop_words:
            continue
        word_list.append(word)
#    print word_list
    feature_set.append(word_list)
    class_set.append(row[1])


for i in range(count):
    feature_set[i].append(class_set[i][0])


feature_sets = ef.get_feature_list(feature_set)

'''
i = 0
for row in text:
    feature_set[i].append(row[0].split(" "))
    feature_set[i].append(row[1])
print feature_set
'''
def get_training_data():
    return feature_sets[:]


def get_test_data():
    return feature_sets[:]

