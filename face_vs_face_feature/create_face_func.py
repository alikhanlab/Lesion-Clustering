#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:48:09 2019

@author: alikhannurlanuly
"""

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



