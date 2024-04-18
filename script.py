import re
from collections import Counter
from nltk.corpus import stopwords

# Function to remove stopwords and punctuations, and count word frequencies
def count_word_frequencies(text):
    # Download NLTK stopwords if not already downloaded
    import nltk
    nltk.download('stopwords')
    
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    word_counts = Counter(filtered_words)
    return word_counts

# Read the contents of the "random_paragraphs.txt" file
with open("./random_paragraphs.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Count word frequencies after removing stopwords
word_frequencies = count_word_frequencies(text)

# Display word frequency count to the console
for word, frequency in word_frequencies.most_common():
    print(f"{word}: {frequency}")
