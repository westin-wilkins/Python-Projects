import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("data.csv")

X_train, X_test, y_train, y_test = train_test_split(df['radius_mean'], df['diagnosis'], random_state=0)

X_train = np.array(X_train).reshape(-1, 1)
X_test = np.array(X_test).reshape(-1, 1)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# Values for prediction
X_new = np.array([[25.22], [2.9], [1], [30]])

prediction = knn.predict(X_new)

# Plotting the radius values
plt.scatter(X_train, y_train, c=y_train, cmap='viridis')
plt.scatter(X_new, prediction, label='Predicted Data')

plt.xlabel('Radius Mean')
plt.ylabel('Diagnosis')
plt.legend()
plt.title('Radius Mean vs Diagnosis')

# 0 mean Benign | 1 means Malignant
print("Prediction: {}".format(prediction))

# Prints accuracy 
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

plt.show()

