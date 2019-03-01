# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:33:31 2019

@author: vianney
"""

import random
import pandas as pd
import os
import numpy as np

file_path = r"C:\Users\vianney\Desktop\projet_python\RATP_GTFS_METRO_10"

class Station(object):
    """
    an object modelizing a station according to gtfs standards, node of djikstra algo.
    """
    def __init__(self, stop_id, stop_name, stop_desc, stop_lat, stop_lon):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_desc = stop_desc
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
        self.neighbourg = {}
        self.transfert = {}
        self.route = {}


    def compute_duration_to_every_neighbourg(self, date, time):
    	"""
    	returns a dictionnary of {[the neighbourg's stop_id] and [duration to get to there]}
    	"""
        #return 0
#    
#    def add_trip(self, route_id, set_of_dates, time, next_stop_id, duration):
#    	"""
#    	returns the name of the line used to make the trip
#    	To be completed
#    	"""
#    	1+1
#        return
#
#	def add_transfert(self, next_stop_id, duration):
#		"""
#		add a transfert to the line. ie : just a trip inside the station : 
#		-> no dependance to time.
#    	returns the name of the line used to make the trip
#    	To be completed
#    	"""
#		return #name_of_line
#


