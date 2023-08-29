import gensim
from gensim import corpora
import pandas as pd
import spacy
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the English NLP model from spaCy
nlp = spacy.load('en_core_web_sm')

df = pd.read_csv("BA_reviews_cleaned.csv")

# Function to preprocess the reviews
def preprocess(text):
    doc = nlp(text)
    # Tokenize, lemmatize, and remove stop words and non-alphabetic words
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return tokens

# Preprocess the reviews
tokens = df['reviews'].apply(preprocess)

# Create a dictionary and corpus needed for Topic Modeling
dictionary = corpora.Dictionary(tokens)
corpus = [dictionary.doc2bow(text) for text in tokens]

# Build the LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, random_state=100, passes=15)

# Print the identified topic words
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic: {idx} \nWords: {topic}\n")

# Calculate sentiment
df['sentiment'] = df['reviews'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Create a WordCloud object
wordcloud = WordCloud(font_path='/path/to/your/font.ttf', background_color='white', max_words=100, contour_width=5, contour_color='blue').generate(" ".join(df['reviews']))

# Plot the WordCloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()