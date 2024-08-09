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


text = """With Morgath's redemption, the Everwood was restored to its former glory, and the realms found harmony once more. Elara stood before the mirror, knowing that her journey had come to an end, yet feeling a deep connection to the world she had discovered.
As she prepared to return to Willowbrook, Faelan spoke with gratitude and admiration. "You have shown us the power of kindness and the strength that lies within the human spirit, Elara. The Everwood will always remember you as its true guardian."
With a final farewell, Elara stepped through the mirror, back into the attic where her adventure had begun. The world around her felt different now, infused with a sense of wonder and possibility. The mirror, now just an ordinary piece of glass, reflected her image, but Elara knew that she carried the magic of the Everwood within her heart.
In the days that followed, Elara shared her story with the villagers of Willowbrook, inspiring them to look beyond the surface of their everyday lives and seek the extraordinary in the ordinary. Though she had returned to her humble village, Elara knew that her spirit was forever entwined with the mysteries of the world beyond the mirror—a world where anything was possible.
And so, the girl in the mirror became a legend in Willowbrook, a tale passed down through generations, reminding all who heard it that the greatest adventures often begin with a simple reflection."""

result = extractive_summary(text)
print(result)
