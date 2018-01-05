__author__ = 'prakhardogra'

def get_feature_set(string):
    return dict([(word,True) for word in string.split(" ")])