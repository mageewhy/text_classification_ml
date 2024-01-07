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

# Disabling warnings:
import warnings 
warnings.filterwarnings('ignore')

# Load train data
data_path = os.path.join(os.path.dirname(__file__), 'training_dataset/newsCorpora.csv')
col_names = ["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
dataset = pd.read_csv(data_path, delimiter='\t', encoding='utf-8', names=col_names)

# Prepare data for training ONLY using Title and Category
training_dataset = dataset[['TITLE', 'CATEGORY']]
training_dataset.to_csv('training_dataset/training_data.csv', index=False)