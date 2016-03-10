#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
from sklearn import svm;
clf=svm.SVC(C=10000.0,kernel="rbf");
t0=time();
clf.fit(features_train,labels_train);
t1=time()-t0;
print "Training time ",round(t1,3),"s";
t1=time();
test1=clf.predict(features_test);
t2=time()-t1;
print "Testing time " , round(t2,3),"s";
count = 0 ;
for i in range(len(test1)):
   count+=test1[i];
print count
from sklearn.metrics import accuracy_score
#########################################################
### your code goes here ###
print accuracy_score(test1,labels_test);
#########################################################

