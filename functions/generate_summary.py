from collections import Counter

import nltk
nltk.download('stopwords')
nltk.download('punkt')

def generate_summary(text):
    """ Generates a summary of a given text """

    sentence_data = get_sentence_data(text)

    summary = get_summary(sentence_data)

    return summary

### Helper Functions ###
def get_words(text):
    """ Returns a list of stemmed words from a given text """

    # Convert text to a list of words (not including punctation)
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)

    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words("english"))
    non_stop_words = filter(lambda word: word not in stop_words, words)

    # Convert each word to its stem
    ps = nltk.stem.PorterStemmer()
    stemmed_words = list(map(lambda word: ps.stem(word), non_stop_words))

    return stemmed_words

def score_sentence(sentence, frequencies):
    """ Returns a score for a sentence using a given frequencies dictionary """

    words = get_words(sentence)
    score = sum(frequencies[word] for word in words) / len(words)
    return score

def get_sentence_data(text):
    """ Returns a list of dictionaries that holds each sentence and its score """

    # Get word frequencies
    stemmed_words = get_words(text)
    frequencies = Counter(stemmed_words)

    # List of sentences in text
    sentences = nltk.tokenize.sent_tokenize(text)

    return [{'sentence': sentence, 'score': score_sentence(sentence, frequencies)} for sentence in sentences]

def get_summary(sentence_data):
    """ Returns a summary using the given sentence data """

    # Find the sentence score threshold (limit to top 3 sentences)
    scores = list(map(lambda data: data['score'], sentence_data))
    threshold = sorted(scores, reverse = True)[2]

    summary_sentence_data = filter(lambda data: data['score'] >= threshold, sentence_data)
    summary_sentences = map(lambda data: data['sentence'], summary_sentence_data)

    return ' '.join(summary_sentences)