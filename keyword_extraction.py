import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def get_keywords(text, n=5):

    # Ensure the stopwords are downloaded
    nltk.download('stopwords')
    nltk.download('punkt')

    # Tokenize the document
    tokens = word_tokenize(document)

    # Filter out the stop words
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english') and word.isalpha()]

    # Create a frequency distribution
    freq_dist = FreqDist(filtered_tokens)

    keywords = [word for word, freq in freq_dist.most_common(n)]
    keyword_sentence = ', '.join(keywords)

    return keyword_sentence


# Sample text
document = """With Morgath's redemption, the Everwood was restored to its former glory, and the realms found harmony once more. Elara stood before the mirror, knowing that her journey had come to an end, yet feeling a deep connection to the world she had discovered.
As she prepared to return to Willowbrook, Faelan spoke with gratitude and admiration. "You have shown us the power of kindness and the strength that lies within the human spirit, Elara. The Everwood will always remember you as its true guardian."
With a final farewell, Elara stepped through the mirror, back into the attic where her adventure had begun. The world around her felt different now, infused with a sense of wonder and possibility. The mirror, now just an ordinary piece of glass, reflected her image, but Elara knew that she carried the magic of the Everwood within her heart.
In the days that followed, Elara shared her story with the villagers of Willowbrook, inspiring them to look beyond the surface of their everyday lives and seek the extraordinary in the ordinary. Though she had returned to her humble village, Elara knew that her spirit was forever entwined with the mysteries of the world beyond the mirror—a world where anything was possible.
And so, the girl in the mirror became a legend in Willowbrook, a tale passed down through generations, reminding all who heard it that the greatest adventures often begin with a simple reflection."""

result = get_keywords(document)

print(result)