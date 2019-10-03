#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 23:20:42 2019

@author: alikhannurlanuly
"""

from calculate_edge_func import calculate_edge
from create_edge_func import create_edge
from import_df_func import import_to_df

import pandas as pd
import numpy as np

xyz_loc = '../result/S01/T2/t01/S01_T2_t01_id_to_xyz.csv'
neighbor_loc = '../result/S01/T2/t01/S01_T2_t01_face_neighbors.csv'

def edge_count_main(xyz_loc, neighbor_loc):
    
    df = import_to_df(xyz_loc, neighbor_loc)
    df = create_edge(df)
    df = calculate_edge(df)
    
    # Dtop edge coordinates
    cols = [i for i in range(3, 15)]
    df.drop(df.columns[cols],axis=1,inplace=True)
    
    # Save to csv file
    name = './' + xyz_loc[:32]+'calculate_edge.csv'
    df.to_csv(name, encoding='utf-8', index = False)
    
    return 

edge_count_main(xyz_loc, neighbor_loc)
    
    
    