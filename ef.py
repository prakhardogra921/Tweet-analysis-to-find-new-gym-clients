__author__ = 'prakhardogra'

import random

import nltk

# this function takes a list of string and returns a set of features
def get_feature_list(documents):
    random.shuffle(documents)
    all_words = []

    for w in documents:

        for word in w[:-2]:

            all_words.append(word)

    all_words = nltk.FreqDist(all_words)
    word_features = list(all_words.keys())

    def find_features(document):
        words = set(document)
        features = {}
        for w in word_features:
            features[w] = (w in words)
        return features

    feature_sets = [(find_features(i[:-2]), i[-1]) for i in documents]
    return feature_sets
