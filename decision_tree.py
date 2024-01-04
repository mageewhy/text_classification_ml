import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.preprocessing import LabelEncoder
import os
import matplotlib.pyplot as plt

# Disabling warnings:
import warnings
warnings.filterwarnings('ignore')

# Load data
data_path = os.path.join(os.path.dirname(__file__), 'training_dataset/newsCorpora.csv')
col_names = ["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
dataset = pd.read_csv(data_path, delimiter='\t', encoding='utf-8', names=col_names)

# Prepare data for training
training_dataset = dataset[['TITLE', 'CATEGORY']]

# Encode the target labels
y_train = training_dataset["CATEGORY"]
le = LabelEncoder()
y_encoded = le.fit_transform(y_train)

# TF-IDF vectorization for text data
tfidf = TfidfVectorizer()
x_train = tfidf.fit_transform(training_dataset['TITLE'])

# Train model using decision tree
clf = DecisionTreeClassifier(max_depth=3)  # Set max_depth to limit the tree depth
clf = clf.fit(x_train, y_encoded)

# Visualize the decision tree
from sklearn.tree import plot_tree

plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=tfidf.get_feature_names_out())
plt.title("Decision tree trained on all Title Features")
plt.show()
