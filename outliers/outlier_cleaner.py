#!/usr/bin/python

import math;
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    for i in range(0,len(predictions)):
        if ((math.fabs(predictions[i]-net_worths[i])<85 )):
           #print predictions[i]-net_worths[i];
            cleaned_data.append((ages[i],net_worths[i],math.fabs(predictions[i]-net_worths[i])));
            

    ### your code goes here

    #print len(cleaned_data);
    return cleaned_data

