import random
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import socket
import spacy
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk, pos_tag, word_tokenize, sent_tokenize
from nltk.tree import Tree
import Relations
from nltk.corpus import stopwords, wordnet as wn, opinion_lexicon
import truecase
from gingerit.gingerit import GingerIt
from bert_implementation import predict_gender

def replace_withname(query, name):
    tokens = word_tokenize(query)
    modified_tokens = []
    for token in tokens:
        if token.lower() in ['i', 'me', 'my', 'mine']:
            modified_tokens.append(name)
        else:
            modified_tokens.append(token)
    final_sent = " ".join(modified_tokens)
    return final_sent

def NER(text, user):
    text = replace_withname(text, user)
    nltk_results = ne_chunk(pos_tag(word_tokenize(text)))
    name_rel = []
    for nltk_result in nltk_results:
        if len(name_rel) == 3:
            Relations.create_relation(name_rel)
            name_rel.clear()
        if len(nltk_result) > 1:
            tag = nltk_result[1]
            if type(tag) != tuple:
                if tag.startswith("N") or tag.startswith("V"):
                    rel = Relations.relationships()
                    if nltk_result[0].upper() in rel:
                        name_rel.append(nltk_result[0].upper())
        if type(nltk_result) == Tree:
            for nltk_result_leaf in nltk_result.leaves():
                name_rel.append(nltk_result_leaf[0])
                gender = predict_gender(nltk_result_leaf[0])
                Relations.create_Node(nltk_result_leaf[0], gender)
            
def autospell(text):
    # Correct spelling using gingerit
    parser = GingerIt()
    nlp = spacy.load('en_core_web_sm')
    # Restore proper casing using truecase
    final_text = truecase.get_true_case(text)
    corrected_text = parser.parse(final_text)['result']
    doc = nlp(corrected_text)
    if not doc[-1].text.endswith('?') and not any(token.tag_ == 'WDT' for token in doc):
        if doc[-1].text not in ['.', '!']:
            if doc[-1].is_sent_start:
                corrected_text += '.'
            elif doc[-1].is_title:
                corrected_text += '.'
            elif doc[-1].is_quote:
                corrected_text += '.'
            elif doc[-1].pos_ in ['NOUN', 'PROPN', 'VERB', 'ADJ', 'ADV']:
                corrected_text += '.'
    return corrected_text


def word_synonyms(word):
    syno = []
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            syno.append(lemma.name())
    return syno


def sentence(query):
    query = sent_tokenize(query)
    return query


def print_random_string(strings):
    random_string = random.choice(strings)
    return random_string


def chart(query):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(query)
    values = list(sentiment_scores.values())
    return values


def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    sentiment = sentiment_scores['compound']

    if sentiment >= 0.05:
        return 'Positive'
    elif sentiment <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


def detect_emotion(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [
        token for token in tokens if token.isalnum() and token not in stop_words]
    emotion_scores = {'joy': 0, 'sadness': 0, 'anger': 0, 'fear': 0}
    for token in filtered_tokens:
        if token in opinion_lexicon.positive():
            emotion_scores['joy'] += 1
        if token in opinion_lexicon.negative():
            emotion_scores['sadness'] += 1
        if token in word_synonyms("angry") or token in word_synonyms("anger"):
            emotion_scores['anger'] += 3
        if token in word_synonyms("fear") or token in word_synonyms("fearful"):
            emotion_scores['fear'] += 4

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    return dominant_emotion


def extract_topics(texts):
    texts = sent_tokenize(texts)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = [word_tokenize(text.lower()) for text in texts]
    clean_tokens = [[lemmatizer.lemmatize(token) for token in tokens if token.isalnum(
    ) and token not in stop_words] for tokens in tokens]
    documents = [' '.join(tokens) for tokens in clean_tokens]

    # Part-of-speech tagging
    tagged_tokens = [pos_tag(word_tokenize(text)) for text in texts]

    # Named Entity Recognition
    named_entities = [ne_chunk(tagged) for tagged in tagged_tokens]

    # Topic modeling
    vectorizer = CountVectorizer(lowercase=False)
    dtm = vectorizer.fit_transform(documents)
    lda = LatentDirichletAllocation(n_components=1, random_state=42)
    lda.fit(dtm)
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(lda.components_):
        topic_words = [feature_names[i] for i in topic.argsort()[:-6:-1]]
        topics.append(topic_words)

    # Topic Extraction
    final = []
    for i, topic in enumerate(topics):
        topic_words = random.sample(topic, min(len(topic), 2))
        extracted_topic = f"{' '.join(topic_words).capitalize()}"
        final.append(extracted_topic)

    # Combine extracted topics with named entities
    final_with_entities = []
    for i, entities in enumerate(named_entities):
        named_entity_words = [chunk[0] for chunk in entities if hasattr(chunk, 'label')]
        if i < len(final): 
            if named_entity_words:
                topic_with_entities = f"{final[i]} regarding {' '.join([w[0] for w in named_entity_words])}"
                final_with_entities.append(topic_with_entities)
            else:
                final_with_entities.append(final[i])

    return final_with_entities

def getIpAdrress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    s = s.getsockname()[0]
    netaddres = ''
    count = 0
    for bit in s:
        if bit == '.':
            count = count + 1
        netaddres = netaddres + bit
        if count == 3:
            return netaddres

def get_definition(query):
    try:
        syno = word_synonyms(query)
        syn = wn.synsets(query)
        definition = syn[1].definition()
        if syn:
            return (definition + " or may we can say " + syno[0]).capitalize()
    except:
        return None
