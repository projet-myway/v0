# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:33:31 2019

@author: vianney
"""

import random
import pandas as pd
import os
import numpy as np
import datetime as dt

file_path = r"C:\Users\vianney\Desktop\projet_python\RATP_GTFS_METRO_10"

class Station(object):
    """
    an object modelizing a station according to gtfs standards, node of djikstra algo.
    """
    def __init__(self, stop_id=0, stop_name='', stop_desc='', stop_lat=0, stop_lon=0):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_desc = stop_desc
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
        self.neighbourg = set()
        self.transfers = {}
        self.trips=pd.DataFrame(columns=['trip_id','set_of_date','time','next_stop','duration'])

    def add_transfert(self, next_stop_id, duration):
        self.transfers[next_stop_id] = duration

    def add_trip(self, trip_id, set_of_dates, time, next_stop_id, duration):
        newrow = pd.DataFrame([[trip_id, set_of_dates,time,next_stop_id,
                                duration]], columns=[
                                               'trip_id','set_of_date','time','next_stop','duration'])
        self.trips=self.trips.append(newrow, ignore_index=True)
    
    def add_transfer_to_facing_plateform(self, stops):
        to_stop_id=stops[(stops.stop_name==self.stop_name)&(stops.stop_id!=self.stop_id)].stop_id
        self.transfers[to_stop_id]=0
    
    def compute_neighbourg(self):
        self.neighbourg = set(self.trips.next_stop).union(set(self.transfers.keys()))
        
    def add_jp1_trips(self):
        jp1_trips = self.trips
        jp1_trips.departure_time = jp1_trips.departure_time + dt.timedelta(1)
        self.trips.append(jp1_trips)
        
    def compute_duration_to_every_neighbour(self, date, time, include_facing_stop=False, stops=None):
        date0 = dt.date(1900, 1, 1)
        time0 = dt.datetime.combine(date0,time)
        if include_facing_stop:
            self.add_transfer_to_facing_plateform(stops)
        dict_durations = self.transfers
        
        if time > dt.time(23,0):
            self.add_jp1_trips()
            
        self.compute_neighbourg()
        
        studied_trips = self.trips[(
                self.trips.time< time0 +
                dt.timedelta(hours=5.5))&(self.trips.time>=time0)]
    
        for neig in self.neighbourg.intersection(set(self.transfers.keys())):
            time_first_train = min(studied_trips.departure_time[next_stop == neig])
            row_first = studied_trips[studied_trips.departure_time==time_first_train]
            waiting_time = row_first.departure_time - time0
            dict_durations[row_first.next_stop] = waiting_time + row_first.duration
            
        return dict_durations
            
            
                    
        
    
        






