from rake_nltk import Rake
import nltk
import nltk
nltk.download()

nltk.data.path.append("C:\\Users\\rajan\\AppData\\Roaming\\nltk_data")

nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()

# Example usage
note = "Your note text goes here..."
print("Keywords:", extract_keywords(note))

