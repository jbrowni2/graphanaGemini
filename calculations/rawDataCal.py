import os
import json
import pandas as pd
import numpy as np

#Calculation of the slope of a waveform
def cal_slope(data):
    mean = np.nan
    stdev = np.nan
    slope = np.nan
    intercept = np.nan


    sum_x = 0
    sum_x2 = 0
    sum_xy = 0
    sum_y = 0
    mean = 0
    stdev = 0
    isum = 10000

    for i in range(0, 10000, 1):
        # the mean and standard deviation
        temp = data[i] - mean
        mean += temp / (i + 1)
        stdev += temp * (data[i] - mean)

        # linear regression
        sum_x += i
        sum_x2 += i * i
        sum_xy += data[i] * i
        sum_y += data[i]

    slope = (isum * sum_xy - sum_x * sum_y) / (isum * sum_x2 - sum_x * sum_x)
    intercept = (sum_y - sum_x * slope) / isum

    return slope, intercept



def cal_length(data):
    wfLen = 0

    for i, wave in enumerate(data["waveform"]["values"].nda[0:1000]):
        wfLen += len(wave)

    wfLen = wfLen/(i+1)

    return wfLen

def cal_MinMax(data):
    minVal = 66000
    maxVal = 0

    for i, wave in enumerate(data["waveform"]["values"].nda[0:1000]):
        minCheck = np.min(wave)
        maxCheck = np.max(wave)
        if minCheck < minVal:
            minVal = minCheck
        if maxCheck > maxVal:
            maxVal = maxCheck

    return minVal, maxVal


#I have not settled on an algorithim for this,
#  but it is more checking the correct answer.
def cal_Duplicate(data):
    duplicateLong = 0
    duplicateTime = 0

    """
    for i,wave in enumerate(data["waveform"]["values"].nda):
        if i >= len(data["waveform"]["values"].nda)-1:
            break
        for wave2 in data["waveform"]["values"].nda[i::]:
            chiArr = wave2 - wave

            chi2 = sum(chiArr**2)

            if chi2 < 1:
                duplicateLong += 1

    """
    uniqArr = np.unique(data["waveform"]["values"].nda, axis=0)
    duplicateLong = len(data["waveform"]["values"].nda) - len(uniqArr)

    """
    times = np.sort(data["timestamp"].nda)

    for i,time in enumerate(times):
        if i >= len(data["waveform"]["values"].nda)-1:
            break
        check = times[i+1] - time

        if check < 1:
            duplicateTime += 1

    """

    uniqTimes = np.unique(data["timestamp"].nda)
    duplicateTime = len(data["timestamp"].nda) - len(uniqTimes)

    return duplicateLong, duplicateTime
    
def cal_baseRMS(data):
    rmsArr = np.zeros(len(data["waveform"]["values"].nda))
    for i,wave in enumerate(data["waveform"]["values"].nda):
        rmsArr[i] = np.sqrt(np.mean(wave[0:1000]**2))

    rms = np.mean(rmsArr)

    return rms

        