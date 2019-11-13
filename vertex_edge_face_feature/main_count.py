import numpy as np
import pandas as pd
import ast
import sys
sys.path.insert(1, '/Users/alikhannurlanuly/Lesion-Clustering/vertex_face_feature/')
from vertex_functions import create_vertex, calculate_vertex
sys.path.insert(1, '/Users/alikhannurlanuly/Lesion-Clustering/edge_face_feature/')
from edge_functions import create_edge, calculate_edge
sys.path.insert(1, '/Users/alikhannurlanuly/Lesion-Clustering/face_face_feature/')
from face_functions import create_face, calculate_face

# Sample of working files
xyz_loc = '../result/S01/T2/t01/S01_T2_t01_id_to_xyz.csv'
neighbor_loc = '../result/S01/T2/t01/S01_T2_t01_face_neighbors.csv'

def vertex_edge_face(xyz_loc, neighbor_loc):
    
    df = pd.read_csv(xyz_loc)
    df_nei = pd.read_csv(neighbor_loc)
    df['face_neighbors'] = df_nei['face_neighbors']
    df['xyz'] = df['xyz'].apply(lambda xyz: ast.literal_eval(xyz))
    df['face_neighbors'] = df['face_neighbors'].apply(lambda face_neighbors: ast.literal_eval(face_neighbors))
    
    #vertex_face
    df_v = create_vertex(df.copy())
    df_v = calculate_vertex(df_v)
    df_v.drop(columns = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8'], inplace = True)
    
    #edge_face
    df_e = create_edge(df.copy())
    df_e = calculate_edge(df_e)
    cols = [i for i in range(3, 15)]
    df_e.drop(df_e.columns[cols],axis=1,inplace=True)
    
    #face_face
    df_f = create_face(df.copy())
    df_f = calculate_face(df_f)
    cols = [i for i in range(3, 9)]
    df_f.drop(df_f.columns[cols],axis=1,inplace=True)
    
    df_main = pd.concat([df, df_v.iloc[:,3:], df_e.iloc[:,3:], df_f.iloc[:,3:]], axis=1, sort=False)
    # Save to csv file
    name = './' + xyz_loc[:32]+'all_count.csv'
    df_main.to_csv(name, encoding='utf-8', index = False)
    
    return

xyz_loc = list(np.load('xyz_loc.npy'))
neighbors_loc = list(np.load('neighbors_loc.npy'))
xyz_loc = ['../'+x for x in xyz_loc]
neighbors_loc = ['../'+x for x in neighbors_loc]

for count, element in enumerate(xyz_loc):
    vertex_edge_face(element, neighbors_loc[count])