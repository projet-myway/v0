# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:14:45 2019

@author: vianney
"""
import pandas as pd
import os
import numpy as np
file_path = r"C:\Users\vianney\Desktop\projet_python\RATP_GTFS_METRO_10"

#f = open("demofile.txt", "r")
ligne10_stopID=pd.read_csv(os.path.join(file_path, "stops.txt"), sep=",")

ligne10_stopID =ligne10_stopID.drop(["stop_code","stop_desc","stop_lat","stop_lon","location_type","parent_station"], axis=1)


ligne10_times=pd.read_csv(os.path.join(file_path, "stop_times.txt"), sep=",")
ligne10_times =ligne10_times.drop(['arrival_time','stop_headsign','shape_dist_traveled'], axis=1)

def time_to_dest(depart,arrivee,date):
# a transformer en méthode de la classe station
    return 
    
def format_time(df):
    temp = np.zeros(df.shape[0])
    for k in range(df.shape[0]):
        temp[k] = df['departure_time'][k]
        try:
            df['departure_time'][k]=pd.to_datetime(s,format='%H:%M:%S')
        except:
            l = s.split(":")
            assert l[0]=="24"
            s =":".join(l)
            temp[k]=to_datetime(s)
        return temp
format_time(ligne10_times)
#coucou
