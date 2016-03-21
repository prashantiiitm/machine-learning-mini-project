#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
"""
val=0;
for k in enron_data:
    if enron_data[k]["poi"]==1:
        val=val+1;
print val
"""
val=0;
for k in enron_data:
    if enron_data[k]["email_address"]!="NaN":
        val=val+1;
print val
"""
mini =12312121212121;
maxi=0;
for k in enron_data:
     if (enron_data[k]["salary"]!="NaN" and enron_data[k]["salary"]<mini ):
         mini = enron_data[k]["salary"];
     if (enron_data[k]["salary"]!=26704229 and enron_data[k]["salary"]!="NaN" and enron_data[k]["salary"]>maxi ):
         maxi = enron_data[k]["salary"];
print maxi;
print mini;
"""
#print enron_data["PRENTICE JAMES"];
#print enron_data["LAY KENNETH L"];

