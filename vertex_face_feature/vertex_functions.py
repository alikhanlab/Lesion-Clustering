import pandas as pd

def create_vertex(df):
    '''
    Takes df
    Returns df vertex coordinates
    
    # v1 = (+1/2 , +1/2, +1/2)
    # v2 = (+1/2, +1/2, -1/2)
    # v3 = (+1/2, -1/2, +1/2)
    # v4 = (+1/2, -1/2, -1/2)
    # v5 = (-1/2, +1/2, +1/2)
    # v6 = (-1/2, -1/2, +1/2)
    # v7 = (-1/2, +1/2, -1/2)
    # v8 = (-1/2, -1/2, -1/2)
    '''
    
    df['v1'] = df['xyz'].apply(lambda xyz: [xyz[0]+0.5, xyz[1]+0.5, xyz[2]+0.5])
    df['v2'] = df['xyz'].apply(lambda xyz: [xyz[0]+0.5, xyz[1]+0.5, xyz[2]-0.5])
    df['v3'] = df['xyz'].apply(lambda xyz: [xyz[0]+0.5, xyz[1]-0.5, xyz[2]+0.5])
    df['v4'] = df['xyz'].apply(lambda xyz: [xyz[0]+0.5, xyz[1]-0.5, xyz[2]-0.5])
    df['v5'] = df['xyz'].apply(lambda xyz: [xyz[0]-0.5, xyz[1]+0.5, xyz[2]+0.5])
    df['v6'] = df['xyz'].apply(lambda xyz: [xyz[0]-0.5, xyz[1]-0.5, xyz[2]+0.5])
    df['v7'] = df['xyz'].apply(lambda xyz: [xyz[0]-0.5, xyz[1]+0.5, xyz[2]-0.5])
    df['v8'] = df['xyz'].apply(lambda xyz: [xyz[0]-0.5, xyz[1]-0.5, xyz[2]-0.5])
    
    return df

# Calculate vertex function
def calculate_vertex(df):
    '''
    Calculates, counts how many identical vertexes, by face neighbors
    Iterates over voxels.
    '''
    import pandas as pd
    c = df.values.tolist()
    # Counting vertexes
    result = []

    for row in c:
        all_v = row[3:]
        neighbors = row[2]
        counter = [0, 0, 0, 0, 0, 0, 0, 0]

        for element in neighbors:
            checker = c[element][3:]
            
            for count, l in enumerate(all_v):

                if l in checker:
                    counter[count]+=1
        counter = sorted(counter, reverse=True)
        result.append(counter)
    
    # Converting to dataFrame
    df_res = pd.DataFrame(result, columns = ['v1_n' , 'v2_n', 'v3_n', 'v4_n', 'v5_n', 'v6_n', 'v7_n', 'v8_n']) 
    
    # Merge with original dataFrame
    vox = pd.concat([df, df_res], axis=1, sort=False)
    
    return vox







