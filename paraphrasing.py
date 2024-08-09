import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
import random
import string

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def get_synonyms(word, pos):
    """
    Get synonyms for a word with a given POS tag using WordNet.
    """
    synonyms = set()
    for synset in wordnet.synsets(word, pos=pos):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
    return list(synonyms)

def choose_synonym(word, pos):
    """
    Choose a synonym for a given word, ensuring it's different from the original word.
    """
    synonyms = get_synonyms(word, pos)
    if word in synonyms:
        synonyms.remove(word)
    return random.choice(synonyms) if synonyms else word

def get_wordnet_pos(tag):
    """
    Map POS tag to WordNet POS tag.
    """
    tag_map = {
        'NN': wordnet.NOUN,
        'JJ': wordnet.ADJ,
        'VB': wordnet.VERB,
        'RB': wordnet.ADV
    }
    return tag_map.get(tag[:2], None)

def paraphrase_sentence(sentence):
    """
    Paraphrase a sentence by replacing some words with their synonyms.
    """
    words = word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
    paraphrased_words = []

    for word, tag in tagged_words:
        # Determine the WordNet POS tag
        wn_pos = get_wordnet_pos(tag)
        
        # Decide to replace with a synonym or keep the original word
        if wn_pos and word.lower() not in string.punctuation:
            paraphrased_word = choose_synonym(word, wn_pos)
            paraphrased_words.append(paraphrased_word)
        else:
            paraphrased_words.append(word)

    return ' '.join(paraphrased_words)

def paraphrase_text(text):
    """
    Paraphrase a complete text.
    """
    sentences = sent_tokenize(text)
    paraphrased_sentences = [paraphrase_sentence(sentence) for sentence in sentences]
    return ' '.join(paraphrased_sentences)


