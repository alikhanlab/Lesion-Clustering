import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance

xyz_filename = '/Users/alikhannurlanuly/Lesion-Clustering/vertex_edge_face_feature/'
xyz_loc = list(np.load(xyz_filename + 'xyz_loc.npy'))
count_loc = ['../'+x[0:29]+'all_count.csv' for x in xyz_loc.copy()]

def k_means_all_patients():
    created_kmeans = True
    scaler = None
    centroids = None
    for filename in count_loc:
        df = pd.read_csv(filename)
        X = df.iloc[:, 3:]
        X = np.array(X)
        path_to_save = filename[:32] + '26_features_clusters.csv'

        if created_kmeans:
            scaler = StandardScaler()
            scaler.fit(X)
            kmeans = KMeans(n_clusters=10).fit(scaler.transform(X))
            centroids = kmeans.cluster_centers_
            created_kmeans = False

        X = scaler.transform(X)

        distances = [[distance.euclidean(c, x) for c in centroids] for x in X]
        clusters = [np.argmin(d) for d in distances]

        cluster_data = pd.DataFrame(columns=['voxel_id', 'cluster_id'])
        cluster_data['voxel_id'] = df['voxel_id'].values
        cluster_data['cluster_id'] = clusters
        cluster_data.to_csv(path_to_save, index=False)
        
k_means_all_patients()