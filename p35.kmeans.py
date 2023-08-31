import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load and preprocess transaction data
# Replace 'transaction_data.csv' with your actual data file path
data = pd.read_csv('CSV_FILES/transaction_data.csv')

# Select relevant features for clustering
selected_features = ['total_amount_spent', 'frequency_of_visits']

# Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data[selected_features])

# Determine the number of clusters (K)
# You can use methods like the elbow method or silhouette score to find an optimal K

# Apply K-Means clustering
num_clusters = 4  # Adjust this based on your analysis
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(normalized_data)

# Visualize the clusters
plt.scatter(data['total_amount_spent'],
            data['frequency_of_visits'], c=data['cluster'], cmap='rainbow')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.title('Customer Segmentation')
plt.show()
