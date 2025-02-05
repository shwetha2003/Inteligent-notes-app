from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

# Example usage
note = "Your note text goes here..."
sentiment = analyze_sentiment(note)
print("Sentiment:", sentiment)
