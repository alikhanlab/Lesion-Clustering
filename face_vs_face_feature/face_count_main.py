#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:51:27 2019

@author: alikhannurlanuly
"""

import sys
sys.path.append('../')

from calculate_face_func import calculate_face
from create_face_func import create_face
from edge_face_feature.import_df_func import import_to_df

import pandas as pd
import numpy as np

xyz_loc = '../result/S01/T2/t01/S01_T2_t01_id_to_xyz.csv'
neighbor_loc = '../result/S01/T2/t01/S01_T2_t01_face_neighbors.csv'

def face_count_main(xyz_loc, neighbor_loc):
    
    df = import_to_df(xyz_loc, neighbor_loc)
    df = create_face(df)
    df = calculate_face(df)
    
    # Dtop edge coordinates
    cols = [i for i in range(3, 9)]
    df.drop(df.columns[cols],axis=1,inplace=True)
    
    # Save to csv file
    name = './' + xyz_loc[:32]+'calculate_face.csv'
    df.to_csv(name, encoding='utf-8', index = False)
    
    return 

face_count_main(xyz_loc, neighbor_loc)