#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:42:03 2019

@author: alikhannurlanuly
"""

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

