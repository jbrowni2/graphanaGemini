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

from pygama import flow
from pygama.raw.build_raw import build_raw
from pygama.dsp.build_dsp import build_dsp


def pRaw(file):
    daqDir = "/Users/gemini/data/daq"
    rawDir = "/Users/gemini/data/raw"
    filePathDaq = daqDir + "/" + str(file)
    filePathRaw= rawDir + "/" + str(file) + ".lh5"

    config = "/Users/gemini/graphanaGemini/IOFunctions/configRaw.json"
    with open(config, 'r') as read_file:
        configure = json.load(read_file)

    configure["ORSIS3316WaveformDecoder"]["MUVT"]["out_stream"] = filePathRaw
    configure["ORiSegHVCardDecoderForHV"]["HV1"]["out_stream"] = filePathRaw
    

    build_raw(filePathDaq, "ORCA", configure, overwrite=True)

def pDsp(file):
    dspDir = "/Users/gemini/data/dsp"
    rawDir = "/Users/gemini/data/raw"
    filePathDsp = dspDir + "/" + str(file) + ".lh5"
    filePathRaw= rawDir + "/" + str(file) + ".lh5"

    chan_file = "/Users/gemini/graphanaGemini/IOFunctions/chan_config.json"
    with open(chan_file) as f:
                chan_conf = json.load(f, object_pairs_hook=OrderedDict)

    build_dsp(filePathRaw, filePathDsp, chan_config = chan_conf, write_mode = 'r')


