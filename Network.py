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

class Network(object):
    """
    an object modelizing a station according to gtfs standards, node of djikstra algo.
    """
    def __init__(self, stop_id, stop_name, stop_desc, stop_lat, stop_lon):
        """
        ????
        """

    def compute_shortes_path(from_stop_name, to_stop_name, date_and_time):
    	"""
    	returns a dictionnary of {[the neighbourg's stop_id] and [duration to get to there]}
    	"""
        return[(stop_id, type_ (ie: n_ligne ou transfert,duration)]