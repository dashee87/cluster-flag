""" clusterFlag: Reproduce country flags with numpy and pandas
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from clusterflag.country_flags import *
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering, DBSCAN

# for reproducibility
np.random.seed(50)


# construct toy dataset based on the cross flag
dataset0 = cross_flag(npoints=[100,1000,500,250,0], 
                        colours=['']*5)
# convert pandas dataframe to numpy array (format for clustering algorithms)
np_dataset0 = dataset0[['x','y']].values
# build k-means model with 4 cluster on this dataset
d0_kmeans = KMeans(n_clusters=4).fit(np_dataset0)

# plot the output
fig, (ax1,ax2)  = plt.subplots(1,2, figsize=(12, 6), dpi=80)
ax1.set_axis_bgcolor('#e6e6e6')
ax1.set_title('Original Data',size=14)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_ylim([0,1])
ax1.set_xlim([0,1.5])
ax1.scatter(dataset0['x'], dataset0['y'], c='black',marker='o',linewidths=0.0)
ax2.set_axis_bgcolor('#e6e6e6')
ax2.set_title('k-means (n=4)',size=14)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_ylim([0,1])
ax2.set_xlim([0,1.5])
ax2.scatter(np_dataset0[:,0], np_dataset0[:,1], 
            c=d0_kmeans.predict(np_dataset0), marker='o', linewidths=0.0)
ax2.scatter(d0_kmeans.cluster_centers_[:,0], d0_kmeans.cluster_centers_[:,1], 
            c='white' ,marker='o', s=500)
plt.show()

# k-means performed pretty well so let's give it a more difficult dataset

# construct toy dataset based on the crescent flag
dataset1 = crescent_flag(npoints=[1000,1000,100,500,500],rect=0.2,ratio=1.5,
                           colours=['']*5,
                           bcx=0.35, bcy=0.5, 
                           scx=0.4, scy=0.5, bradius=0.25, sradius=0.2, 
                           starcx=0.5, starcy=0.5, starrx=0.125, 
                           starry=0.125)
np_dataset1 = dataset1[['x','y']].values

# kmeans model with 4 clusters
d1_kmeans = KMeans(n_clusters=4).fit(np_dataset1)
# plot the output
fig, (ax1,ax2)  = plt.subplots(1,2, figsize=(12, 6), dpi=80)
ax1.set_axis_bgcolor('#e6e6e6')
ax1.set_title('Original Data',size=14)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_ylim([0,1])
ax1.set_xlim([0,1.5])
ax1.scatter(dataset1['x'], dataset1['y'], c='black', marker='o', linewidths=0)
ax2.set_axis_bgcolor('#e6e6e6')
ax2.set_title('k-means (n=4)',size=14)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_ylim([0,1])
ax2.set_xlim([0,1.5])
ax2.scatter(np_dataset1[:,0], np_dataset1[:,1], 
            c=d0_kmeans.predict(np_dataset1), marker='o', linewidths=0.0)
ax2.scatter(d1_kmeans.cluster_centers_[:,0], d1_kmeans.cluster_centers_[:,1], 
            c='white' ,marker='o', s=500)
plt.show()

# k-means did not perform so well, so we'll try Hierarchical clustering
# and DBSCAN

# hierarchical clustering (n=4) with ward linkage
d1_hc = AgglomerativeClustering(linkage='ward',
                                     n_clusters=4).fit_predict(np_dataset1)
# DBSCAN
d1_db = DBSCAN(eps=0.04, min_samples=5).fit_predict(np_dataset1)
fig, (ax1,ax2)  = plt.subplots(1,2, figsize=(12, 6), dpi=80)
ax1.set_axis_bgcolor('#e6e6e6')
ax1.set_title('Agglomerative (Ward) Clustering (n=4)',size=14)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_ylim([0,1])
ax1.set_xlim([0,1.5])
ax1.scatter(np_dataset1[:,0], np_dataset1[:,1], c=d1_hc, 
            marker='o', linewidths=0)
ax2.set_axis_bgcolor('#e6e6e6')
ax2.set_title('DBSCAN (eps=0.04, minPts=5)',size=14)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_ylim([0,1])
ax2.set_xlim([0,1.5])
ax2.scatter(np_dataset1[:,0], np_dataset1[:,1], 
            c=d1_db, marker='o', linewidths=0.0)
plt.show()
