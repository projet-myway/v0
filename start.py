# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:14:45 2019

@author: vianney
"""
import pandas as pd
import os
import numpy as np
import pdb
import Station as st


#file_path = r"C:\Users\vianney\Desktop\projet_python\RATP_GTFS_METRO_10"
file_path = r"C:\Users\vianney\Documents\GitHub\MyWay\v1\RATP_GTFS_LINES\RATP_GTFS_METRO_10"
#f = open("demofile.txt", "r")
ligne10_stopID0=pd.read_csv(os.path.join(file_path, "stops.txt"), sep=",")
ligne10_stopID0 = ligne10_stopID0.drop(["stop_code","location_type","parent_station"], axis=1)
ligne10_stopID =ligne10_stopID0.drop(["stop_desc","stop_lat","stop_lon"], axis=1)


ligne10_times=pd.read_csv(os.path.join(file_path, "stop_times.txt"), sep=",")
ligne10_times =ligne10_times.drop(['arrival_time','stop_headsign','shape_dist_traveled'], axis=1)

ligne10_times = pd.merge(ligne10_times, ligne10_stopID, how='left', on=['stop_id'])
a=ligne10_times.iloc[:,-3:-1].drop_duplicates()
ligne10_stopID1 = pd.merge(ligne10_stopID0, a, how='inner', on = ['stop_id'])




 

def time_to_dest(depart,arrivee,date):
# a transformer en méthode de la classe station
    return 
    
def convert_24_to_datetime(df):
    
    a=df['departure_time'].str.extract(r'(?P<hour>\d{2}):(?P<minute>\d{2})')
    a['hour']=a['hour'].apply(int)%24
    a['hour']=a['hour'].apply(str)
    a['instr']=a['hour']+':'+a['minute']+":00"
    a['instr']=pd.to_datetime(a['instr'],format='%H:%M:%S')
    df['departure_time']=a['instr']
    
    
convert_24_to_datetime(ligne10_times)

def build_all_stations(df):
    # takes all items of the stopID dataset to build stations
    l = []
    for index, row in df.iterrows():
        l.append(st.Station(row['stop_id'], row['stop_name'], row['stop_desc'], row['stop_lat'], row['stop_lon']))     
        if index == 60:
            pdb.set_trace()
    return l


l = build_all_stations(ligne10_stopID1)