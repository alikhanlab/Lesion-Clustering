#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:46:48 2019

@author: alikhannurlanuly
"""

# Import necessary functions:
from vertex_functions import separate_xyz, create_vertex_coordinates, calculate_vertex

# Sample of working files
xyz_loc = 'result/S01/T2/t01/S01_T2_t01_id_to_xyz.csv'
neighbor_loc = 'result/S01/T2/t01/S01_T2_t01_face_neighbors.csv'


def vertex_count(xyz_loc, neighbor_loc):
    '''
    Given xyz and face nighbor location, compute v1_n,...,v8_n
    Counts number of identical vertexes by face neighbor per voxel
    '''
    ##### Step 1
    import pandas as pd
    
    # x, y, z coordinates of every voxel 
    df = pd.read_csv(xyz_loc)
    voxel_id = df['voxel_id']
    df.drop(columns = ['voxel_id'], inplace = True)

    # face neighbors
    neighbors = pd.read_csv(neighbor_loc)
    neighbors.drop(columns = ['voxel_id', 'num_of_face_neighbors'], inplace = True)
    
    
    #### Step 2
   
    # Separate xyz and add face neighbors
    df = separate_xyz(df)
    df['neighbors'] = neighbors['face_neighbors']
    

    #### Step 3
    
    # Add vertex coordinates to df
    df = create_vertex_coordinates(df)
    
    
    #### Step 4
    
    # Calculate v1_n,...,v8_n
    df_final = calculate_vertex(df)
    df_final.drop(columns = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8'], inplace = True)
    df_final['voxel_id'] = voxel_id
    df_final = df_final.set_index('voxel_id')
    

    #### Step 5
    
    # Save file
    # name = './result/S01/T2/t01/' + xyz_loc[18:29]+'calculate_vertex.csv'
    
    name = './' + xyz_loc[:29]+'calculate_vertex.csv'
    df_final.to_csv(name, encoding='utf-8', index = True)
    
    return 

vertex_count(xyz_loc, neighbor_loc)