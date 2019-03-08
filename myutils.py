# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:11:08 2019

@author: vianney
"""

import pandas as pd
import os
import numpy as np
import pdb
import Station as st
import datetime

def convert_24_to_datetime(df):
    a=df['departure_time'].str.extract(r'(?P<hour>\d{2}):(?P<minute>\d{2})')
    a['hour']=a['hour'].apply(int)%24
    a['hour']=a['hour'].apply(str)
    a['instr']=a['hour']+':'+a['minute']+":00"
    a['instr']=pd.to_datetime(a['instr'],format='%H:%M:%S')
    df['departure_time']=a['instr']
    
def complete_times_with_next_and_duration(ligne10_times):
    #preliminary stage before build_all_trips
    pd.options.mode.chained_assignment = None
    ligne10_times['next_stop']=float('nan')
    ligne10_times['duration']=float('nan')
    a = pd.DataFrame()
    set_id = set(ligne10_times.trip_id)
    for itrip in set_id:
        df_trip = ligne10_times[ligne10_times.trip_id == itrip]
        #isoler le df matchant trip_id
        df_trip['next_stop'][:-1]= df_trip['stop_id'][1:]
        df_trip['duration'][:-1]= (pd.to_datetime((df_trip['departure_time'][1:].values - (df_trip['departure_time'][:-1]).values))).minute
        a = a.append(df_trip)
        #ligne10_times.drop(ligne10_times[ligne10_times.trip_id == itrip].index)
    return a


def build_all_transfers(transfers):
    l = {}
    for index, row in transfers.iterrows():
        from_stop_id = row.from_stop_id
        if from_stop_id in l.keys():
            l[from_stop_id][row.to_stop_id]=datetime.timedelta(minutes=(row.min_transfer_time//60)+1)
        else :
            l[from_stop_id]={row.to_stop_id: datetime.timedelta(minutes=(row.min_transfer_time//60)+1)}
    return l

def build_inter_plateform_transfers(stops):
    df = stops[['stop_id', 'stop_name']]
    df['other_platform']=np.zeros(df.shape[0])
    for index, row in df.iterrows():
        row['other_platform']=df[(df.stop_name==row.stop_name.item())&(df.stop_id!=row.stop_id)].stop_id  
    return df

interplat = build_inter_plateform_transfers(stops)
        
    #ajouter les transfers change-quai
#dict_transfer = build_all_transfers(transfers)

def trip_get_route_id_and_set_of_date(stop_id, trip_id, trips, calendar, calendar_expt):
    rowtrip = trips[trips.trip_id==trip_id][:]
    route_id = rowtrip.route_id
    trip_serviceid = int(rowtrip.service_id)
    row = calendar[calendar.service_id==trip_serviceid][:]
    sod = set(pd.date_range(row.start_date.item(), row.end_date.item()).tolist())
    sod.difference_update(set(calendar_expt[calendar_expt.service_id == trip_serviceid].date))
    return route_id, sod

def build_all_trips2(times, trips, calendar, calendar_expt):
    #à utiliser avec times[times.stop_id==station.stop_id]
    k=0
    df=pd.DataFrame(columns=['trip_id','set_of_date','time','next_stop','duration'])
    for index, row in times.iterrows():
        if k<10:
            k+=1
            routeid, sod = trip_get_route_id_and_set_of_date(row.stop_id, row.trip_id, trips, calendar, calendar_expt)
            if not pd.isna(row.duration):
                newrow = pd.DataFrame([[row.trip_id,
                                       sod,row.departure_time,row.next_stop,
                                       datetime.timedelta(minutes=row.duration)]], columns=[
                                               'trip_id','set_of_date','time','next_stop','duration'])
                df=df.append(newrow, ignore_index=True)
    return df

#df_100trips = build_all_trips2(times, trips, calendar, calendar_expt) ok

def build_all_stations(df_stops):
    # takes all items of the stopID dataset to build stations
    # df_trips à filtrer à 0;+5h ensuite pour ne pas alourdir.
    l = {}
    for index, row in df_stops.iterrows():
        newstation = st.Station(row['stop_id'], row['stop_name'], row['stop_desc'], row['stop_lat'], row['stop_lon'])
        l[row.stop_id] = newstation
    return l

def add_trips_and_transfers_to_each_station(times, dict_transfer, dict_stations, calendar, calendar_expt):
    for cle, val in dict_stations:
        val.trips = build_all_trips2(times[times.stop_id==cle],
                                        trips, calendar, calendar_expt)
        val.transfer = dict_transfer[val.stop_id]