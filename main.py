import sys
import os
import io
import json
import argparse
import numpy as np
import pandas as pd
import h5py
from pprint import pprint
from collections import OrderedDict
import matplotlib.pyplot as plt
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/gemini/graphanaGemini')

import IOFunctions.readData as read
import calculations.rawDataCal as rdc
import calculations.dspDataCal as ddc

from pygama import flow
from pygama.raw.build_raw import build_raw
from pygama.dsp.build_dsp import build_dsp


def main():

    #Here we do all of the raw data calculations
    
    dataRaw = read.get_raw_data(9189, "Card1")

    numDupLong, numDupTime = rdc.cal_Duplicate(dataRaw)

    slope, intercept = rdc.cal_slope(dataRaw["waveform"]["values"].nda[0][0:10000])
    
    wfLen = rdc.cal_length(dataRaw)

    minVal, maxVal = rdc.cal_MinMax(dataRaw)

    rms = rdc.cal_baseRMS(dataRaw)

    

    #Here we do all of the dsp data calculations
    dataDsp = read.get_df(9189, "Card1")
    dataDsp = dataDsp[dataDsp["timestamp"] > 0]
    dataDsp = dataDsp[dataDsp["timestamp"] < 161806772310837]
    dataDsp = dataDsp.drop_duplicates()
    dataDsp = dataDsp.sort_values(["timestamp"])

    rate = ddc.cal_trigger_rate(dataDsp)



    





if __name__ == "__main__":
    main()
