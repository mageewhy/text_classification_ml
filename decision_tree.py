import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.metrics import classification_report

# Import Webscraping
import webscraping as ws

# Disabling warnings:
import warnings 
warnings.filterwarnings('ignore')

# Load data
data_path = os.path.join(os.path.dirname(__file__), 'training_dataset/newsCorpora.csv')
col_names = ["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
dataset = pd.read_csv(data_path, delimiter='\t', encoding='utf-8', names=col_names)

# Prepare data for training
training_dataset = dataset[['TITLE', 'CATEGORY']]

X = training_dataset["TITLE"]
Y = training_dataset["CATEGORY"]
# x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
x_train = X
y_train = Y

# Test Data set from Webscraping
test_dataset = ws.headlines_with_categories



# Encode the target labels
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)
y_test_encoded = le.transform(y_test)

# TF-IDF vectorization for text data
tfidf = TfidfVectorizer()   
x_train_tfidf = tfidf.fit_transform(x_train)
x_test_tfidf = tfidf.transform(test_dataset)

# Train model using decision tree on the TF-IDF transformed data
DTclf = DecisionTreeClassifier(max_depth=15) 
DTclf = DTclf.fit(x_train_tfidf, y_train_encoded)

# Make predictions on the test set
y_pred = DTclf.predict(x_test_tfidf)

# Model Evaluation
print("\n\n")
print(classification_report(y_test_encoded, y_pred))





# Scatterplot Visualization

# # Reduce dimensions using TruncatedSVD (similar to PCA for sparse data)
# svd = TruncatedSVD(n_components=2, random_state=42)
# x_train_tfidf_2d = svd.fit_transform(x_train_tfidf)

# # Create a DataFrame for visualization
# df = pd.DataFrame(x_train_tfidf_2d, columns=['Component 1', 'Component 2'])
# df['Category'] = y_train_encoded

# # Scatter plot
# plt.figure(figsize=(8, 6))
# sns.scatterplot(data=df, x='Component 1', y='Component 2', hue='Category', palette='viridis')
# plt.title('2D Scatter Plot of TF-IDF Data (TruncatedSVD)')
# plt.xlabel('Component 1')
# plt.ylabel('Component 2')
# plt.legend(title='Category')
# plt.show()

# # Visualize the decision tree
# plt.figure(figsize=(12, 8))
# plot_tree(DTclf, filled=True, feature_names=tfidf.get_feature_names_out())
# plt.title("Decision tree trained on all Title Features")
# plt.show()
