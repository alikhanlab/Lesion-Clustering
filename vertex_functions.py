#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:54:33 2019

@author: alikhannurlanuly
"""

# Separate xyz function
def separate_xyz(df):
    '''
    Separating x, y, z for each every column
    '''
    import pandas as pd
    xyz_list=list(df['xyz'])
    clean_xyz_str = [xyz_list[count].strip('(').strip(')').split(', ') for count, val in enumerate(xyz_list)]
    clean_xyz_int = [ [ int(l) for l in x ] for x in clean_xyz_str ]
    coordinates = pd.DataFrame(clean_xyz_int)
    coordinates.columns = ["x", "y", "z"]
    df = coordinates.copy()
    
    return df 

# Create vertex coordinates function
def create_vertex_coordinates(df):
    '''
    # Assume separated x,y,z dataframe
    # Our feature vertexes are:

    # v1 = (+1/2 , +1/2, +1/2)
    # v2 = (+1/2, +1/2, -1/2)
    # v3 = (+1/2, -1/2, +1/2)
    # v4 = (+1/2, -1/2, -1/2)
    # v5 = (-1/2, +1/2, +1/2)
    # v6 = (-1/2, -1/2, +1/2)
    # v7 = (-1/2, +1/2, -1/2)
    # v8 = (-1/2, -1/2, -1/2)
    
    This function builds these vertex coordinates
    '''
    import pandas as pd
    coordinates = df.copy()
    
    #########################
    # v1 feature
    v100 = ((coordinates['x'] + 1/2, coordinates['y'] + 1/2, coordinates['z'] + 1/2))
    coordinates['v11'] = v100[0]
    coordinates['v12'] = v100[1]
    coordinates['v13'] = v100[2]
    v1 = list(coordinates[['v11', 'v12', 'v13']].itertuples(index=False, name=None))
    coordinates['v1'] = v1
    coordinates.drop(columns=['v11', 'v12', 'v13'], inplace=True)
    
    #########################
    # v2 feature 
    v200 = ((coordinates['x'] + 1/2, coordinates['y'] + 1/2, coordinates['z'] - 1/2))
    coordinates['v21'] = v200[0]
    coordinates['v22'] = v200[1]
    coordinates['v23'] = v200[2]
    v2 = list(coordinates[['v21', 'v22', 'v23']].itertuples(index=False, name=None))
    coordinates['v2'] = v2
    coordinates.drop(columns=['v21', 'v22', 'v23'], inplace=True)
    
    #########################
    # v3 feature
    v300 = ((coordinates['x'] + 1/2, coordinates['y'] - 1/2, coordinates['z'] + 1/2))
    coordinates['v31'] = v300[0]
    coordinates['v32'] = v300[1]
    coordinates['v33'] = v300[2]
    v3 = list(coordinates[['v31', 'v32', 'v33']].itertuples(index=False, name=None))
    coordinates['v3'] = v3
    coordinates.drop(columns=['v31', 'v32', 'v33'], inplace=True)
    
    #########################
    # v4 feature
    v400 = ((coordinates['x'] + 1/2, coordinates['y'] - 1/2, coordinates['z'] - 1/2))
    coordinates['v41'] = v400[0]
    coordinates['v42'] = v400[1]
    coordinates['v43'] = v400[2]
    v4 = list(coordinates[['v41', 'v42', 'v43']].itertuples(index=False, name=None))
    coordinates['v4'] = v4
    coordinates.drop(columns=['v41', 'v42', 'v43'], inplace=True)
    
    #########################
    # v5 feature
    v500 = ((coordinates['x'] - 1/2, coordinates['y'] + 1/2, coordinates['z'] + 1/2))
    coordinates['v51'] = v500[0]
    coordinates['v52'] = v500[1]
    coordinates['v53'] = v500[2]
    v5 = list(coordinates[['v51', 'v52', 'v53']].itertuples(index=False, name=None))
    coordinates['v5'] = v5
    coordinates.drop(columns=['v51', 'v52', 'v53'], inplace=True)
    
    #########################
    # v6 feature
    v600 = ((coordinates['x'] - 1/2, coordinates['y'] - 1/2, coordinates['z'] + 1/2))
    coordinates['v61'] = v600[0]
    coordinates['v62'] = v600[1]
    coordinates['v63'] = v600[2]
    v6 = list(coordinates[['v61', 'v62', 'v63']].itertuples(index=False, name=None))
    coordinates['v6'] = v6
    coordinates.drop(columns=['v61', 'v62', 'v63'], inplace=True)
    
    #########################
    # v7 feature
    v700 = ((coordinates['x'] - 1/2, coordinates['y'] + 1/2, coordinates['z'] - 1/2))
    coordinates['v71'] = v700[0]
    coordinates['v72'] = v700[1]
    coordinates['v73'] = v700[2]
    v7 = list(coordinates[['v71', 'v72', 'v73']].itertuples(index=False, name=None))
    coordinates['v7'] = v7
    coordinates.drop(columns=['v71', 'v72', 'v73'], inplace=True)
    
    #########################
    # v8 feature
    v800 = ((coordinates['x'] - 1/2, coordinates['y'] - 1/2, coordinates['z'] - 1/2))
    coordinates['v81'] = v800[0]
    coordinates['v82'] = v800[1]
    coordinates['v83'] = v800[2]
    v8 = list(coordinates[['v81', 'v82', 'v83']].itertuples(index=False, name=None))
    coordinates['v8'] = v8
    coordinates.drop(columns=['v81', 'v82', 'v83'], inplace=True)
    
    return coordinates

# Calculate vertex function
def calculate_vertex(df):
    '''
    Calculates, counts how many identical vertexes, by face neighbors
    Iterates over voxels.
    '''
    import pandas as pd
    # ast for converting str to list
    import ast
    c = df.values.tolist()
    # Counting vertexes
    result = []

    for row in c:
        all_v = row[4:12]
        neighbors = row[3]
        neighbors = ast.literal_eval(neighbors)
        counter = [0, 0, 0, 0, 0, 0, 0, 0]

        for element in neighbors:
            checker = c[element][4:12]
            
            for count, l in enumerate(all_v):

                if l in checker:
                    counter[count]+=1

        result.append(counter)
    
    # Converting to dataFrame
    df_res = pd.DataFrame(result, columns = ['v1_n' , 'v2_n', 'v3_n', 'v4_n', 'v5_n', 'v6_n', 'v7_n', 'v8_n']) 
    
    # Merge with original dataFrame
    vox = pd.concat([df, df_res], axis=1, sort=False)
    
    return vox







