import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(sentence):
    # Use the polarity_scores method to get the sentiment scores
    sentiment_scores = sia.polarity_scores(sentence)
    
    # Extract the compound score which indicates overall sentiment
    compound_score = sentiment_scores['compound']
    
    # Determine sentiment category based on compound score
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment

# Example sentence
sentence = "I love this new phone, it's amazing!"

# Get sentiment analysis
sentiment = analyze_sentiment(sentence)

# Output the result
print(f"Overall Sentiment: {sentiment}")
