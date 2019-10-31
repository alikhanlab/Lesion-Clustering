#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:30:36 2019

@author: alikhannurlanuly
"""
# Import necessary functions:
from count_identical_vertexes_by_face import vertex_count

def vertex_count_all_files():
    '''
    This function runs vertex_count() function accross given directory
    In this project we have 46 patients, for every patients up-to 24 mri-exam days
    Basicly, runs over 46*24 = 1104 files
    '''
    import os
    from glob import iglob

    rootdir_glob = 'Macintosh HD/Users/alikhannurlanuly/Lesion Categorization/Assignment 1/**/*_clusters.csv' # Note the added asterisks
    
    # This will return absolute paths
    file_xyz_list = [f for f in sorted(iglob('**/*_id_to_xyz.csv', recursive=True)) if os.path.isfile(f)]
    file_neighbors_list = [f for f in sorted(iglob('**/*_face_neighbors.csv', recursive=True)) if os.path.isfile(f)]
    
    for count, element in enumerate(file_xyz_list):
    
        vertex_count(element, file_neighbors_list[count])