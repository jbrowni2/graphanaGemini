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
import time
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/gemini/graphanaGemini')

import IOFunctions.readData as read
import IOFunctions.processData as procData
import calculations.rawDataCal as rdc
import calculations.dspDataCal as ddc
import calculations.dspMUVTCal as dmc
import SQL_functions.insertVals as IV

from pygama import flow
from pygama.raw.build_raw import build_raw
from pygama.dsp.build_dsp import build_dsp


def main():

    """
    file = os.listdir("/Users/gemini/data/daq")[1]
    seconds = time.time()
    #procData.pRaw(file)
    #procData.pDsp(file)

    #Here we do all of the raw data calculations for Ge detectors
    dataRaw = read.get_raw_data("Run9189", "Card1")

    #Here is where I calculate the duplicates for each detector.
    duplicate1, duplicate2, duplicate3, duplicate4, duplicate5, duplicate6, duplicate7, duplicate8 = rdc.cal_Duplicate(dataRaw)
    dupDict = {
        "duplicate1": duplicate1,
        "duplicate2": duplicate2, 
        "duplicate3": duplicate3, 
        "duplicate4": duplicate4, 
        "duplicate5": duplicate5, 
        "duplicate6": duplicate6,
        "duplicate7": duplicate7, 
        "duplicate8": duplicate8,   
        "timestamp":seconds
    }
    IV.insertVal("root", "CEVNSGemini2026$", "gemini", dupDict, tabName="duplicates")


    slope1, intercept1 = rdc.cal_slope(dataRaw["waveform"]["values"].nda[0][0:10000])
    dupDict = {
        "slope1": slope1, "intercept1": intercept1, 
        "slope2": slope1, "intercept2": intercept1, 
        "slope3": slope1, "intercept3": intercept1, 
        "slope4": slope1, "intercept4": intercept1, 
        "slope5": slope1, "intercept5": intercept1, 
        "slope6": slope1, "intercept6": intercept1, 
        "slope7": slope1, "intercept7": intercept1, 
        "slope8": slope1, "intercept8": intercept1, 
        "timestamp":seconds
        }    
    IV.insertVal("root", "CEVNSGemini2026$", "gemini", dupDict, tabName="line")



    wfLen = rdc.cal_length(dataRaw)
    dupDict = {
        "Length": int(wfLen),
        "timestamp":seconds
        }    
    IV.insertVal("root", "CEVNSGemini2026$", "gemini", dupDict, tabName="wfLength")

    minVal, maxVal = rdc.cal_MinMax(dataRaw)
    dupDict = {
        "min": int(minVal), "max": int(maxVal),
        "timestamp":seconds
        }    
    IV.insertVal("root", "CEVNSGemini2026$", "gemini", dupDict, tabName="wfMinMax")

    rms = rdc.cal_baseRMS(dataRaw)
    dupDict = {
        "rms1": float(rms),
        "rms2": float(rms),
        "rms3": float(rms), 
        "rms4": float(rms), 
        "rms5": float(rms),
        "rms6": float(rms),
        "rms7": float(rms),
        "rms8": float(rms),
        "timestamp":seconds
        }    
    IV.insertVal("root", "CEVNSGemini2026$", "gemini", dupDict, tabName="wfRMS")

    

    #Here we do all of the dsp data calculations for germanium detectors
    dataDsp = read.get_df("Run9189", "Card1")
    dataDsp = dataDsp[dataDsp["timestamp"] > 0]
    dataDsp = dataDsp[dataDsp["timestamp"] < 161806772310837]
    dataDsp = dataDsp.drop_duplicates()
    dataDsp = dataDsp.sort_values(["timestamp"])

    rate = ddc.cal_trigger_rate(dataDsp)
    dupDict = {
        "rate": float(rate),
        "timestamp":seconds
        }    
    IV.insertVal("root", "CEVNSGemini2026$", "gemini", dupDict, tabName="geRate")

    #Here we do all of the raw data calculations for MUVT panels

    #Here we do all of the dsp data calculations for MUVT panels

    muvtData = read.get_raw_data(file, "MUVT")
    df = pd.DataFrame({"timestamp": muvtData["timestamp"].nda, "channel":muvtData["channel"].nda})
    df = df[df["timestamp"] > 0]
    df = df[df["timestamp"] < 161806772310837]
    df = df.drop_duplicates()
    df = df.sort_values(["timestamp"])
    coincidence = dmc.coinc_cal(df, 10000)
    dupDict = {
        "coincidence2": int(coincidence[1]),
        "coincidence3": int(coincidence[2]),
        "coincidence4": int(coincidence[3]),
        "coincidence5": int(coincidence[4]),
        "coincidence6": int(coincidence[5]),
        "coincidence7": int(coincidence[6]),
        "coincidence8": int(coincidence[7]),
        "coincidence9": int(coincidence[8]),
        "coincidence10": int(coincidence[9]),
        "coincidence11": int(coincidence[10]),
        "coincidence12": int(coincidence[11]),
        "coincidence13": int(coincidence[12]),
        "coincidence14": int(coincidence[13]),
        "coincidence15": int(coincidence[14]),
        "coincidence16": int(coincidence[15]),
        "timestamp":seconds
        }    
    IV.insertVal("root", "CEVNSGemini2026$", "gemini", dupDict, tabName="muvtCoin")
    
    muvtRate = ddc.cal_trigger_rate(df)
    dupDict = {
        "rate": float(muvtRate),
        "timestamp":seconds
        }    
    IV.insertVal("root", "CEVNSGemini2026$", "gemini", dupDict, tabName="muvtRate")
    """


    #Here is where we start putting values into a hv database.

    #Here we are going to do the fft of the Ge detcectors.
    dataRaw = read.get_raw_data("Run9189", "Card1")
    pow1, freq1, pow2, freq2, pow3, freq3, pow4, freq4, pow5, freq5, pow6, freq6, pow7, freq7, pow8, freq8 = rdc.cal_fft(dataRaw)










    





if __name__ == "__main__":
    main()
