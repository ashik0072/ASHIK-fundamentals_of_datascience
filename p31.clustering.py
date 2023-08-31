import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess customer data
# Replace 'customer_data.csv' with your actual data
data = pd.read_csv('CSV_FILES/customer_data1.csv')

# Select relevant features for clustering
# demographics [1-young_adult 2-adult 3-teenager ]
selected_features = ['purchase_history', 'browsing_behavior', 'demographics']

# Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data[selected_features])

# Determine the number of clusters (K)
# You can use methods like the elbow method or silhouette score to find an optimal K

# Apply K-Means clustering
num_clusters = 5  # Adjust this based on your analysis
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(normalized_data)

# Visualize the clusters (for example, using pair plots)
# sns.pairplot(data, hue='cluster', diag_kind='kde')
# plt.show()

# Analyze characteristics of each cluster
cluster_means = data.groupby('cluster').mean()
print(cluster_means)

# Use these clusters for targeted marketing strategies
