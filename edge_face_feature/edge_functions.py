import pandas as pd

def create_edge(df):
    '''
    Takes df
    Returns df edges' coordinates
    '''
    df['edge_1'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]+0.5, xyz[1]+0.5, xyz[2]+0.5],[xyz[0]+0.5, xyz[1]+0.5, xyz[2]-0.5]]))
    df['edge_2'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]+0.5, xyz[1]+0.5, xyz[2]+0.5],[xyz[0]+0.5, xyz[1]-0.5, xyz[2]+0.5]]))

    df['edge_3'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]+0.5, xyz[1]-0.5, xyz[2]+0.5],[xyz[0]+0.5, xyz[1]-0.5, xyz[2]-0.5]]))
    df['edge_4'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]+0.5, xyz[1]-0.5, xyz[2]-0.5],[xyz[0]+0.5, xyz[1]+0.5, xyz[2]-0.5]]))

    df['edge_5'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]+0.5, xyz[1]+0.5, xyz[2]-0.5],[xyz[0]-0.5, xyz[1]+0.5, xyz[2]-0.5]]))
    df['edge_6'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]+0.5, xyz[1]-0.5, xyz[2]-0.5],[xyz[0]-0.5, xyz[1]-0.5, xyz[2]-0.5]]))

    df['edge_7'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]+0.5, xyz[2]+0.5],[xyz[0]-0.5, xyz[1]+0.5, xyz[2]-0.5]]))
    df['edge_8'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]-0.5, xyz[2]+0.5],[xyz[0]-0.5, xyz[1]+0.5, xyz[2]+0.5]]))

    df['edge_9'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]-0.5, xyz[2]+0.5],[xyz[0]-0.5, xyz[1]-0.5, xyz[2]-0.5]]))
    df['edge_10'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]-0.5, xyz[2]+0.5],[xyz[0]+0.5, xyz[1]-0.5, xyz[2]+0.5]]))

    df['edge_11'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]-0.5, xyz[2]-0.5],[xyz[0]-0.5, xyz[1]+0.5, xyz[2]-0.5]]))
    df['edge_12'] = df['xyz'].apply(lambda xyz: sorted([[xyz[0]-0.5, xyz[1]+0.5, xyz[2]+0.5],[xyz[0]+0.5, xyz[1]+0.5, xyz[2]+0.5]]))

    return df

def calculate_edge(df):
    '''
    Takes df with edge coordinates
    Calculates, counts how many identical edges, by face neighbors
    Iterates over voxels
    Returns df with counted identical edges
    '''
    c = df.values.tolist()
    result = []
    
    for row in c:
        all_e = row[3:]
        neighbors = row[2]
        counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for element in neighbors:
            checker = c[element][3:]
            
            for count, l in enumerate(all_e):

                if l in checker:
                    counter[count]+=1
        counter = sorted(counter, reverse=True)
        result.append(counter)
        
    df_res = pd.DataFrame(result, columns = ['e1_n' , 'e2_n', 'e3_n', 'e4_n', 'e5_n', 'e6_n', 'e7_n', 'e8_n', 'e9_n', 'e10_n', 'e11_n', 'e12_n']) 
    edg = pd.concat([df, df_res], axis=1, sort=False)
    
    return edg

