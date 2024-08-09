import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict
import string

nltk.download('punkt')
nltk.download('stopwords')

def extractive_summary(text, num_sentences=3):
    # Tokenize the text into words and sentences
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    
    # Create a frequency table for words
    stop_words = set(stopwords.words('english'))
    word_freq = defaultdict(int)
    
    for word in words:
        word = word.lower()
        if word not in stop_words and word not in string.punctuation:
            word_freq[word] += 1

    # Calculate sentence scores based on word frequencies
    sentence_scores = defaultdict(int)
    
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] += word_freq[word]
    
    # Select the top num_sentences sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join(summary_sentences)
    
    return summary


