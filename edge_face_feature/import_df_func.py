#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:35:41 2019

@author: alikhannurlanuly
"""

import pandas as pd
import numpy as np

xyz_loc = '../result/S01/T2/t01/S01_T2_t01_id_to_xyz.csv'
neighbor_loc = '../result/S01/T2/t01/S01_T2_t01_face_neighbors.csv'

def import_to_df(xyz_loc, neighbor_loc):
    '''
    Takes xyz_loc, neighbor_loc
    
    Returns df
    '''
    def from_str_to_list(xyz):
        # from str to array
        import ast
        
        xyz = list(ast.literal_eval(xyz))
        
        return xyz
    
    df = pd.read_csv(xyz_loc)
    face_neighbors = pd.read_csv(neighbor_loc)
    df['face_neighbors'] = face_neighbors['face_neighbors']
    df['xyz'] = df['xyz'].apply(from_str_to_list)
    
    return df

df = import_to_df(xyz_loc, neighbor_loc)



