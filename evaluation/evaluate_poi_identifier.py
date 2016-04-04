#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
import numpy as np;
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features, labels, test_size=0.30, random_state=42);

from sklearn import tree;
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score,recall_score;
clf2=tree.DecisionTreeClassifier();
clf2.fit(features,labels);
sc2=clf2.predict(features);
prec=precision_score(labels,sc2);
print prec;
#print np.sum(sc2==labels)
#print len(labels)

clf=tree.DecisionTreeClassifier();
clf.fit(features_train,labels_train);
sc=clf.predict(features_test);
prec2=precision_score(labels_test,sc);
print prec2;
rec2=recall_score(labels_test,sc);
print rec2;
#print sc;



print clf.score(features_test,labels_test);

### your code goes here 


