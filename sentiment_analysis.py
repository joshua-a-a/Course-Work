import pandas as pd
import spacy
from textblob import TextBlob

# loading the spaCy model, english core web small
nlp = spacy.load('en_core_web_sm')

# the function to preprocess text, which removes stop words and punctuation, then converts the text to lowercase, tokenizes the text and joins the tokens back together
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

# my function to analyze sentiment, using TextBlob to calculate the sentiment score and classify as positive, negative or neutral
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    
    # classifying the sentiment based on the score
    if sentiment_score > 0.1:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# testing the functions before running on the dataset 
sample_reviews = [
    "This product is amazing!",
    "This was okay, but not great.",
    "I'm really disappointed with this product."]

# testing the preprocess_text function
for review in sample_reviews:
    sentiment = analyze_sentiment(review)
    print(f"This review: '{review}' is: {sentiment}")

# define the data types for columns 1 and 10
dtype = {1: str, 10: str}

# load the data, specifying the data types
df = pd.read_csv('.venv/amazon_product_reviews.csv', dtype=dtype)

# dropping rows with missing values in the 'reviews.text' column 
clean_data = df.dropna(subset=['reviews.text']).copy()

# preprocessing the reviews and analyzing sentiment 
clean_data.loc[:, 'cleaned_reviews'] = clean_data['reviews.text'].apply(preprocess_text)
clean_data.loc[:, 'sentiment'] = clean_data['cleaned_reviews'].apply(analyze_sentiment)

# the final product
print(clean_data[['reviews.text', 'sentiment']].head(20))      
