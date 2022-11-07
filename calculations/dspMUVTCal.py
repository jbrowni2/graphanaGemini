import os
import json
import pandas as pd
import numpy as np

def coinc_cal(data, deltaT):
    coincPanel = np.zeros(16)
    numChannels = 2

    for i, time in enumerate(data["timestamp"]):
        coincNum = 0
        j = i + 1
        if j >= len(data["timestamp"]):
            break


        check = (data["timestamp"].iloc[j] - time)*8
        while check <= deltaT:
            if data["channel"].iloc[j] != data["channel"].iloc[i]:
                coincNum += 1
            j += 1
            check = (data["timestamp"].iloc[j] - time)*8
        
        if coincNum >= numChannels:
            coincNum = numChannels - 1
        
        coincPanel[coincNum] += 1
    
    return coincPanel

