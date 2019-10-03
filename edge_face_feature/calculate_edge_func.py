#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 23:16:12 2019

@author: alikhannurlanuly
"""

def calculate_edge(df):
    '''
    Takes df with edge coordinates
    Calculates, counts how many identical edges, by face neighbors
    Iterates over voxels
    Returns df with counted identical edges
    '''
    import pandas as pd
    import ast
    c = df.values.tolist()
    # Counting edge
    result = []

    for row in c:
        all_e = row[3:]
        neighbors = row[2]
        neighbors = ast.literal_eval(neighbors)
        counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for element in neighbors:
            checker = c[element][3:]
            
            for count, l in enumerate(all_e):

                if l in checker:
                    counter[count]+=1

        result.append(counter)
    
    # Converting to dataFrame
    df_res = pd.DataFrame(result, columns = ['e1_n' , 'e2_n', 'e3_n', 'e4_n', 'e5_n', 'e6_n', 'e7_n', 'e8_n', 'e9_n', 'e10_n', 'e11_n', 'e12_n']) 
    
    # Merge with original dataFrame
    edg = pd.concat([df, df_res], axis=1, sort=False)
    
    return edg