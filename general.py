# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:01:54 2019

@author: vianney
"""
import pandas as pd
import os
import numpy as np
import pdb
import Station as st
import datetime
import myutils as mu

file_path = r"C:\Users\vianney\Documents\GitHub\MyWay\v1\RATP_GTFS_LINES\RATP_GTFS_METRO_10"

# 1) import [stops, stop_times, calendar , calendar_dates, routes  transfers trips] as df

#stops
stops = pd.read_csv(os.path.join(file_path, "stops.txt"), sep=",")
stops = stops.drop(['stop_code', 'location_type', 'parent_station'], axis=1)

#stop_times
times = pd.read_csv(os.path.join(file_path, "stop_times.txt"), sep=",")
times = times.drop(['arrival_time','stop_headsign','shape_dist_traveled'], axis=1)
mu.convert_24_to_datetime(times)
times = mu.complete_times_with_next_and_duration(times)

#calendar
calendar = pd.read_csv(os.path.join(file_path, "calendar.txt"), sep=",")
calendar['start_date'] = pd.to_datetime(calendar['start_date'], format = '%Y%m%d')
calendar['end_date'] = pd.to_datetime(calendar['end_date'], format ='%Y%m%d')
calendar = calendar.drop(['monday','tuesday','wednesday','thursday','friday','saturday','sunday'], axis=1)

#calendar_dates
calendar_expt = pd.read_csv(os.path.join(file_path, "calendar_dates.txt"), sep=",")
calendar_expt = calendar_expt.drop(['exception_type'], axis=1)
calendar_expt['date'] = pd.to_datetime(calendar_expt['date'], format ='%Y%m%d')

#routes
routes = pd.read_csv(os.path.join(file_path, "routes.txt"), sep=",")

#transfers
transfers = pd.read_csv(os.path.join(file_path, "transfers.txt"), sep=",")
transfers = transfers.drop(['transfer_type'], axis=1)
transfers = transfers.drop(transfers[(transfers.from_stop_id>9999 ) | (transfers.to_stop_id>9999)].index )

#trips
trips = pd.read_csv(os.path.join(file_path, "trips.txt"), sep=",")
trips = trips.drop(['trip_headsign','trip_short_name','direction_id','shape_id'], axis=1)

#dict_of_station = build_all_stations(stops)
# à faire : déjà dans start mais à améliorer.
# replit le dico avec clef = stop_id, val = objet stations
# seuls les stop_id,name,desc,lon,lat sont remlis (lisibles direct)
# restent les attributs trips = dict: clef = 
print('ok1')
dict_transfer = mu.build_all_transfers(transfers)
print('ok2')
df_of_trips = mu.build_all_trips2(times, trips, calendar, calendar_expt)#just_for_test
print('ok3')
dict_stations = mu.build_all_stations(stops)
#key = 
print('-----end_general.py------') # OK jusqu'ici le 7/03

mu.add_trips_and_transfers_to_each_station(times, dict_transfer, dict_stations, calendar, calendar_expt)
