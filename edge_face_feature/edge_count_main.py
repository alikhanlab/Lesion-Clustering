from edge_functions import create_edge, calculate_edge
import pandas as pd
import numpy as np
import ast

xyz_loc = '../result/S01/T2/t01/S01_T2_t01_id_to_xyz.csv'
neighbor_loc = '../result/S01/T2/t01/S01_T2_t01_face_neighbors.csv'

def edge_count(xyz_loc, neighbor_loc):
    '''
    Counts identical edges in vertexes
    '''
    df = pd.read_csv(xyz_loc)
    df_nei = pd.read_csv(neighbor_loc)
    df['face_neighbors'] = df_nei['face_neighbors']
    df['xyz'] = df['xyz'].apply(lambda xyz: ast.literal_eval(xyz))
    df['face_neighbors'] = df['face_neighbors'].apply(lambda face_neighbors: ast.literal_eval(face_neighbors))
    
    df = create_edge(df)
    df = calculate_edge(df)

    # Dtop edge coordinates
    cols = [i for i in range(3, 15)]
    df.drop(df.columns[cols],axis=1,inplace=True)
    
    # Save to csv file
    name = './' + xyz_loc[:32]+'edge_count.csv'
    df.to_csv(name, encoding='utf-8', index = False)
    
    return 

edge_count(xyz_loc, neighbor_loc)
    
    
    