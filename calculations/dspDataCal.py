import os
import json
import pandas as pd
import numpy as np

def cal_trigger_rate(data):
    return len(data["timestamp"][1000::])/((max(data["timestamp"][1000::]) - min(data["timestamp"][1000::]))*8e-9)