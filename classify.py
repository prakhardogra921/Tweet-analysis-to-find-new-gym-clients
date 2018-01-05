__author__ = 'prakhardogra'

import os
import gttd
import nltk
import pickle
import time
#import numpy as np
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
import numpy as np

'''
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
'''
training_data = gttd.get_training_data()
testing_data = gttd.get_test_data()

def get_classifier_NB(training_data):

    fname = "NB_classify"
    if os.path.isfile(fname):
        file_fp = open("NB_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        classifier = nltk.NaiveBayesClassifier.train(training_data)
        file_fp = open("NB_classify", "wb")
        pickle.dump(classifier, file_fp)
        file_fp.close()
        return classifier

def get_classifier_MNB(training_data):

    fname = "MNB_classify"
    if os.path.isfile(fname):
        file_fp = open("MNB_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        classifier = SklearnClassifier(MultinomialNB())
        classifier.train(training_data)
        file_fp = open("MNB_classify", "wb")
        pickle.dump(classifier, file_fp)
        file_fp.close()
        return classifier


def get_classifier_BNB(training_data):

    fname = "BNB_classify"
    if os.path.isfile(fname):
        file_fp = open("BNB_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        classifier = SklearnClassifier(BernoulliNB())
        classifier.train(training_data)
        file_fp = open("BNB_classify", "wb")
        pickle.dump(classifier, file_fp)
        file_fp.close()
        return classifier


def get_GNB(training_data):

    fname = "GNB_classify"
    # We need trainin data in the form of Numpy array
    # so the following processing needs to be done
    Y = [int(i[-1]) for i in training_data]
    training_data = [list(i) for i in training_data]
    lim = len(training_data)
    for i in range(0, lim):
        training_data[i] = list(training_data[i][0].values())
    X = training_data
    if os.path.isfile(fname):
        file_fp = open("GNB_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        cf = GaussianNB()
        cf.fit(X, Y)
        file_fp = open("GNB_classify", "wb")
        pickle.dump(cf, file_fp)
        file_fp.close()
        return cf


def classify_with_GNB(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_GNB(training_data)
    t = cf.score(X, Y) * 100
    print("GaussianNB accuracy percent:", t)
    return t


def get_SVM(training_data):

    fname = "SVM_classify"
    # We need trainin data in the form of Numpy array
    # so the following processing needs to be done
    Y = [int(i[-1]) for i in training_data]
    training_data = [list(i) for i in training_data]
    lim = len(training_data)
    for i in range(0, lim):
        training_data[i] = list(training_data[i][0].values())
    X = training_data
    if os.path.isfile(fname):
        file_fp = open("SVM_classify", "rb")
        classifier = pickle.load(file_fp)
        file_fp.close()
        return classifier
    else:
        cf = svm.SVC()
        cf.fit(X, Y)
        file_fp = open("SVM_classify", "wb")
        pickle.dump(cf, file_fp)
        file_fp.close()
        return cf


def classify_with_SVM(training_data, testing_data):
    Y = [int(i[-1]) for i in testing_data]
    testing_data = [list(i) for i in testing_data]
    lim = len(testing_data)
    for i in range(0, lim):
        testing_data[i] = list(testing_data[i][0].values())
    X = testing_data
    X = np.array(X)
    Y = np.array(Y)
    cf = get_SVM(training_data)
    t = cf.score(X, Y) * 100
    print("SVM accuracy percent:", cf.score(X, Y) * 100)
    return t

def get_class_data():
    all_algo = []
    start_time = time.time()
    svm_acc = classify_with_SVM(training_data, testing_data)
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("SVM", svm_acc, time_taken))
    print("Time Taken by SVM in seconds : ", time_taken)
    start_time = time.time()
    nb_acc = nltk.classify.accuracy(get_classifier_NB(training_data), testing_data) * 100
    print("NB Accuracy percent = ", nb_acc)
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("NB", nb_acc, time_taken))
    print("Time Taken by NB in seconds : ", time_taken)
    start_time = time.time()
    mnb_acc = nltk.classify.accuracy(get_classifier_MNB(training_data), testing_data) * 100
    print("MultinomialNB accuracy percent:", mnb_acc)
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("MNB", mnb_acc, time_taken))
    print("Time Taken by MultinomialNB in seconds : ", time_taken)
    start_time = time.time()
    bnb_acc = nltk.classify.accuracy(get_classifier_BNB(training_data), testing_data) * 100
    print("BernoulliNB accuracy percent:", bnb_acc)
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("BNB", bnb_acc, time_taken))
    print("Time Taken by BernoulliNB in seconds : ", time_taken)
    start_time = time.time()
    # print("GaussianNB accuracy percent:",nltk.classify.accuracy(getget_classifier_GNB(training_data), testing_data)*100)
    gnb_acc = classify_with_GNB(training_data, testing_data)
    end_time = time.time()
    time_taken = end_time - start_time
    all_algo.append(("GNB", gnb_acc, time_taken))
    print("Time Taken by GaussianNB in seconds : ", time_taken)
    return all_algo

#get_class_data()