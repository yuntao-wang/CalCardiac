# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:22:36 2018

@author: Yuntao Wang
"""

def get_window (signals, annotation, sec):
    """
    this function gives a sec-seconds window (sec seconds before, sec seconds after the annotation mark)
    of the ECG signals and assign value 1 if it's PVC beat and 0 otherwise.
    parameter: signals: numpy array containing heart beat record values
               annotation: wfdb.annotation object containing heart beat annotations
               sec: positive integer number indicating the half-width of the window
    return: two lists
            siglist: a list of lists of length 360*2*sec 
            annlist: a list containing 1 if PVC beat, 0 otherwise
    """
    siglist = []
    annlist = []
    
    #loop through the annotation.symbol list
    for i in range(len(annotation.symbol)):
        timestamp = annotation.sample[i] #get the timestamp
        
        #test if that timestamp can have sec seconds before and after window
        windowStart = timestamp - sec*annotation.fs
        windowEnd = timestamp + sec*annotation.fs
        if windowStart >= 0 & windowEnd <= len(signals):
            if annotation.symbol[i] == 'V':
                # check if the length of this strip is 360*2*sec
                if len(signals[windowStart:windowEnd,].flatten().tolist()) == 2*sec*annotation.fs:
                    siglist.append(signals[windowStart:windowEnd,].flatten().tolist())
                    annlist.append(1)
                else:
                    continue
            else:
                # check if the length of this strip is 360*2*sec
                if len(signals[windowStart:windowEnd,].flatten().tolist()) == 2*sec*annotation.fs:
                    siglist.append(signals[windowStart:windowEnd,].flatten().tolist())
                    annlist.append(0)
        else:
            continue
    
    return siglist, annlist