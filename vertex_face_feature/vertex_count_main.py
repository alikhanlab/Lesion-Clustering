from vertex_functions import create_vertex, calculate_vertex
import pandas as pd
import ast
    
# Sample of working files
xyz_loc = '../result/S01/T2/t01/S01_T2_t01_id_to_xyz.csv'
neighbor_loc = '../result/S01/T2/t01/S01_T2_t01_face_neighbors.csv'

def vertex_count(xyz_loc, neighbor_loc):
    '''
    Given xyz and face nighbor location, compute v1_n,...,v8_n
    Counts number of identical vertexes by face neighbor per voxel
    '''
    df = pd.read_csv(xyz_loc)
    df_nei = pd.read_csv(neighbor_loc)
    df['face_neighbors'] = df_nei['face_neighbors']
    df['xyz'] = df['xyz'].apply(lambda xyz: ast.literal_eval(xyz))
    df['face_neighbors'] = df['face_neighbors'].apply(lambda face_neighbors: ast.literal_eval(face_neighbors))
    #### Step 3
    # Add vertex coordinates to df
    df = create_vertex(df)
    
    #### Step 4
    
    df = calculate_vertex(df)
    df.drop(columns = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8'], inplace = True)

    #### Step 5
    # Save file
    # name = './result/S01/T2/t01/' + xyz_loc[18:29]+'calculate_vertex.csv'
    
    name = './' + xyz_loc[:32]+'vertex_count.csv'
    df.to_csv(name, encoding='utf-8', index = False)
    
    return 

vertex_count(xyz_loc, neighbor_loc)