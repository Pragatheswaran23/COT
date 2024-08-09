import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def get_keywords(text, n=5):

    # Ensure the stopwords are downloaded
    nltk.download('stopwords')
    nltk.download('punkt')

    # Tokenize the document
    tokens = word_tokenize(text)

    # Filter out the stop words
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english') and word.isalpha()]

    # Create a frequency distribution
    freq_dist = FreqDist(filtered_tokens)

    keywords = [word for word, freq in freq_dist.most_common(n)]
    keyword_sentence = ', '.join(keywords)

    return keyword_sentence
