import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

home_data = pd.read_csv(r"C:\Users\Westin\Downloads\Programming Languages\Python\Portfolio\Projects\Machine Learning\california_housing.csv", usecols = ['longitude', 'latitude', 'median_house_value'])





X_train, X_test, y_train, y_test = train_test_split(home_data[['latitude', 'longitude']], home_data[['median_house_value']], test_size=0.33, random_state=0)
X_train_norm = preprocessing.normalize(X_train)
X_test_norm = preprocessing.normalize(X_test)

kmeans = KMeans(n_clusters = 5, random_state = 0, n_init='auto')
kmeans.fit(X_train_norm)

silhouette_score(X_train_norm, kmeans.labels_, metric='euclidean')

K = range(2, 8)
fits = []
score = []

sns.scatterplot(data = X_train, x = 'longitude', y = 'latitude', hue = kmeans.labels_)
plt.show()

sns.boxplot(x = kmeans.labels_, y = y_train['median_house_value'])
#plt.show()



for k in K:
    # train the model for current value of k on training data
    model = KMeans(n_clusters = k, random_state = 0, n_init='auto').fit(X_train_norm)
    
    # append the model to fits
    fits.append(model)
    
    # Append the silhouette score to scores
    score.append(silhouette_score(X_train_norm, model.labels_, metric='euclidean'))

#Find the best number of clusters
sns.lineplot(x = K, y = score)
#plt.show()
