from LookingDuration.looking import convertTime, get_data, findLookingDuration

import pandas as pd
import numpy as np
import time
import datetime
import csv
import copy
import pytest

PATH = "LookingDuration/test/test_data"

videoData = PATH + "/AD6BMY_JC.csv"
respData = PATH + "/2021-10-07-21-23-AML.csv"


def test_convertTime():
    newTimeFormat = convertTime("00:00:12:345")
    assert(newTimeFormat >=0)

def test_get_data():
    
    fromVideo = get_data(videoData)
    assert(fromVideo.InTime[0]>=0)

def test_findLookingDuration():
    fromVideo = get_data(videoData)
    fromResp = get_data(respData)
    i=2 # trial 5 from resp
    duration = findLookingDuration(fromResp.Start[i], fromResp.End[i], fromVideo.InTime, fromVideo.OutTime, save_duration=False, savetoFile='test.csv').get('Duration')
    assert(duration >=0)


