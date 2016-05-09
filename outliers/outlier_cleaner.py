#!/usr/bin/python

from operator import itemgetter
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []


    ### your code goes here
    error = []
    error = predictions - net_worths
    formatted_data = zip(ages,net_worths,error)
    sortedByError = sorted(formatted_data,key=itemgetter(2))
    cleaned_data = sortedByError[:int(0.9*len(error))]
    return cleaned_data

