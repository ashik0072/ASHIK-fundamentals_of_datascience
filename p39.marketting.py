import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Load the transaction data
# Replace 'transaction_data.csv' with your actual data file path
data = pd.read_csv('CSV_FILES/transaction_data1.csv')

# Select features for clustering
features = ['total_amount_spent', 'number_of_items']

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data[features])

# Determine the number of clusters (K)
# You can use methods like the elbow method or silhouette score to find an optimal K

# Apply K-Means clustering
num_clusters = 4  # Adjust this based on your analysis
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(scaled_features)

# Visualize the clusters
sns.scatterplot(data=data, x='total_amount_spent',
                y='number_of_items', hue='cluster', palette='Set1')
plt.title('Customer Segmentation based on Spending and Purchase Behavior')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.show()
