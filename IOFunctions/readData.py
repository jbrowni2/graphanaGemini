import os
import json
import pandas as pd
import numpy as np
from pygama import __version__ as pygama_version
import pygama
import pygama.lgdo as lgdo
import pygama.lgdo.lh5_store as lh5
from os.path import expanduser
import copy


def get_raw_data(file, tb, buffer_len = 100000000):
    raw_dir = "/Users/gemini/data/raw"

    f_raw = raw_dir + "/Run" + str(file) + ".lh5"

    raw_store = lh5.LH5Store()

    t1_noise, n_rows_read = raw_store.read_object(tb, f_raw, start_row=0, n_rows=buffer_len)

    return t1_noise

def get_dsp_data(file, tb, buffer_len = 100000000):
    raw_dir = "/Users/gemini/data/dsp"

    f_raw = raw_dir + "/Run" + str(file) + ".lh5"

    raw_store = lh5.LH5Store()

    t2_noise, n_rows_read = raw_store.read_object(tb, f_raw, start_row=0, n_rows=buffer_len)

    return t2_noise

def get_df(run, tab=None):
    data = get_dsp_data(run, tab)
    dictionary = dict()
    for col in data:
        dictionary[col] = data[col].nda

    df = pd.DataFrame(data=dictionary)
    return df
