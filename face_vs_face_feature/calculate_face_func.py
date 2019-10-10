#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:50:49 2019

@author: alikhannurlanuly
"""

def calculate_face(df):
    '''
    Calculates, counts how many identical faces, by face neighbors
    Iterates over voxels.
    '''
    import pandas as pd
    import ast
    c = df.values.tolist()
    # Counting edge
    result = []

    for row in c:
        all_f = row[3:]
        neighbors = row[2]
        neighbors = ast.literal_eval(neighbors)
        counter = [0, 0, 0, 0, 0, 0]

        for element in neighbors:
            checker = c[element][3:]
            
            for count, l in enumerate(all_f):

                if l in checker:
                    counter[count]+=1

        result.append(counter)
    
    # Converting to dataFrame
    df_res = pd.DataFrame(result, columns = ['f1_n' , 'f2_n', 'f3_n', 'f4_n', 'f5_n', 'f6_n']) 
    
    # Merge with original dataFrame
    fc = pd.concat([df, df_res], axis=1, sort=False)
    
    return fc