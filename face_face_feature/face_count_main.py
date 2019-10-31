from face_functions import create_face, calculate_face
import pandas as pd
import numpy as np
import ast

xyz_loc = '../result/S01/T2/t01/S01_T2_t01_id_to_xyz.csv'
neighbor_loc = '../result/S01/T2/t01/S01_T2_t01_face_neighbors.csv'

def face_count_main(xyz_loc, neighbor_loc):
    
    df = pd.read_csv(xyz_loc)
    df_nei = pd.read_csv(neighbor_loc)
    df['face_neighbors'] = df_nei['face_neighbors']
    df['xyz'] = df['xyz'].apply(lambda xyz: ast.literal_eval(xyz))
    df['face_neighbors'] = df['face_neighbors'].apply(lambda face_neighbors: ast.literal_eval(face_neighbors))
    df = create_face(df)
    df = calculate_face(df)
    
    # Dtop edge coordinates
    cols = [i for i in range(3, 9)]
    df.drop(df.columns[cols],axis=1,inplace=True)
    
    # Save to csv file
    name = './' + xyz_loc[:32]+'face_count.csv'
    df.to_csv(name, encoding='utf-8', index = False)
    
    return 

face_count_main(xyz_loc, neighbor_loc)