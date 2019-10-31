import pandas as pd

def create_face(df):
    '''
    Takes df
    Returns df face coordinates
    '''    
    
    df['face_1'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]+0.5, xyz[2]+0.5], [xyz[0]+0.5, xyz[1]+0.5, xyz[2]+0.5], [xyz[0]-0.5, xyz[1]-0.5, xyz[2]+0.5], [xyz[0]+0.5, xyz[1]-0.5, xyz[2]+0.5]]))
    df['face_2'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]+0.5, xyz[1]+0.5, xyz[2]+0.5], [xyz[0]+0.5, xyz[1]-0.5, xyz[2]+0.5], [xyz[0]+0.5, xyz[1]-0.5, xyz[2]-0.5], [xyz[0]+0.5, xyz[1]+0.5, xyz[2]-0.5]]))
    df['face_3'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]-0.5, xyz[2]+0.5], [xyz[0]+0.5, xyz[1]-0.5, xyz[2]+0.5], [xyz[0]+0.5, xyz[1]-0.5, xyz[2]-0.5], [xyz[0]-0.5, xyz[1]-0.5, xyz[2]-0.5]]))
    df['face_4'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]+0.5, xyz[2]+0.5], [xyz[0]+0.5, xyz[1]+0.5, xyz[2]+0.5], [xyz[0]+0.5, xyz[1]+0.5, xyz[2]-0.5], [xyz[0]-0.5, xyz[1]+0.5, xyz[2]-0.5]]))
    df['face_5'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]+0.5, xyz[1]-0.5, xyz[2]-0.5], [xyz[0]+0.5, xyz[1]+0.5, xyz[2]-0.5], [xyz[0]-0.5, xyz[1]-0.5, xyz[2]-0.5], [xyz[0]-0.5, xyz[1]+0.5, xyz[2]-0.5]]))
    df['face_6'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]+0.5, xyz[2]+0.5], [xyz[0]-0.5, xyz[1]-0.5, xyz[2]+0.5], [xyz[0]-0.5, xyz[1]-0.5, xyz[2]-0.5], [xyz[0]-0.5, xyz[1]+0.5, xyz[2]-0.5]]))

    return df

def calculate_face(df):
    '''
    Calculates, counts how many identical faces, by face neighbors
    Iterates over voxels.
    '''
    c = df.values.tolist()
    # Counting edge
    result = []

    for row in c:
        all_f = row[3:]
        neighbors = row[2]
        counter = [0, 0, 0, 0, 0, 0]

        for element in neighbors:
            checker = c[element][3:]
            
            for count, l in enumerate(all_f):

                if l in checker:
                    counter[count]+=1
        counter = sorted(counter, reverse=True)
        result.append(counter)
    
    # Converting to dataFrame
    df_res = pd.DataFrame(result, columns = ['f1_n' , 'f2_n', 'f3_n', 'f4_n', 'f5_n', 'f6_n']) 
    
    # Merge with original dataFrame
    fc = pd.concat([df, df_res], axis=1, sort=False)
    
    return fc
