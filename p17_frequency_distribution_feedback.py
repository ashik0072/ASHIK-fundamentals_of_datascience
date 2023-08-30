import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('C://Users//ASHIK C SABU//Desktop//data.csv')

# Preprocess the text data


def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)  # Remove punctuation
    words = text.split()
    stop_words = set(['the', 'and', 'is', 'of', 'to', 'in',
                     'it', 'that', 'you'])  # Sample stop words
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    return words


data['processed_feedback'] = data['feedback'].apply(preprocess_text)

# Calculate the frequency distribution of words
all_words = [word for words in data['processed_feedback'] for word in words]
word_freq = Counter(all_words)

# Get user input for the number of top words to display
N = int(input("Enter the number of top words to display: "))

# Display the top N most frequent words and their frequencies
top_words = word_freq.most_common(N)
for word, freq in top_words:
    print(f"{word}: {freq}")

# Plot a bar graph
top_words, freq = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(top_words, freq)
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title(f'Top {N} Most Frequent Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
