import pandas as pd
import numpy as np
import time
import datetime
import csv


#from decimal import *
def convertTime(TimeString):

  element = datetime.datetime.strptime(TimeString,"%H:%M:%S:%f")
  timestamp = datetime.datetime.timestamp(element) - datetime.datetime.timestamp(datetime.datetime.strptime("1900-0-1",'%Y-%M-%d'))
  return round(timestamp, 3)


def get_data(data):
    """Reads the data as a csv or a pandas DataFrame and returns the DataFrame.
    Although this function is used in other functions to import the data from a csv file,
    this can also work as a stand-alone function for reading a csv file.

    :param data: path to the csv file or pandas DataFrame

    :return: pandas DataFrame.

    :raises ValueError: Check for the file path and make sure the file is a csv file.

    :Example:

    >>> import lookduration as ld
    >>> fromVideo = ld.get_data("AD6BMY_JC.csv")
    >>> fromResp = ld.get_data("2021-10-07-21-23-AML.csv")
    >>> data.shape
   
    """

    try:
        # Checks if the data is not a Pandas Dataframe
        if not isinstance(data, pd.DataFrame):
            # Reads the csv file
            final_data = pd.read_csv(data)

        else:
            final_data = copy.deepcopy(data)

        return final_data
    except ValueError as e:
        print("ValueError: " + str(e))
        raise
 

 
def findLookingDuration(trial_st, trial_end, InTime, OutTime, save_duration=False):
    
    """Returns looking duration.
    ``trial_st`` and ``trial_end`` are start and end of a particular trial.

    :param trial_st: start time of a trial from responses
    :param trial_end: end of a trial from responses
    :param InTime: looking in time stampsvfrom video
    :param OutTime: looking out time stamps from video
    :param save_duration: boolean to save the results. (Default=False)

    :return: looking duration of the trial

    :Example:

    >>> import lookduration as ld
    >>> i=5 # trial 5 from resp
    >>> duration = ld.findLookingDuration(fromResp.Start[i], fromResp.End[i], fromVideo.InTime, fromVideo.OutTime, save_duration=True).get('Duration')
    """

    looking_time = 0
    look_st = 0
    look_end = 0
    st=0
    end=0
    
    try:

        for x in range(len(InTime)):
            if convertTime(InTime[x]) >= float(trial_st): 
                if x==0: st=0
                else: st=x-1
                break

        for x in range(len(OutTime)):
            if convertTime(OutTime[x]) >= float(trial_end): 
                end=x
                break

        if st==end:
            looking_time = float(trial_end)-float(trial_st)
        else: 

            if convertTime(OutTime[st]) >= float(trial_st):
                look_st = convertTime(OutTime[st]) - float(trial_st)
            elif convertTime(OutTime[st]) < float(trial_st):
                st=st+1
                look_st=convertTime(OutTime[st]) - convertTime(InTime[st])


            if (convertTime(InTime[end]) <= float(trial_end)): 
                look_end = float(trial_end) - convertTime(InTime[end]) 
            elif (convertTime(InTime[end]) > float(trial_end)): 
                end = end-1
                look_end= convertTime(OutTime[end]) - convertTime(InTime[end]) 
 
    except ValueError as e:
            print("ValueError: " + str(e))
            raise


    for i in range(st+1, end):
        looking_time = looking_time + convertTime(OutTime[i]) - convertTime(InTime[i]) 

    looking_time = looking_time + look_st + look_end

    if save_duration: 
        with open('lookingduration.csv','a') as fd: 
            fd.write(str(looking_time) + ', ')
            #writer = csv.writer(fd)
            #writer.writerow(str(looking_time))

    return {'st':st, 'end':end, 'Duration':looking_time}
    
