from keyword_extraction import extract_keywords
import wikipediaapi

def generate_insights(text):
    # Specify a custom user agent
    user_agent = "MyNotesProcessor/1.0 (contact: your-email@example.com)"  # Replace with your contact email

    wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="en")  # Add user agent here

    keywords = extract_keywords(text)  # Extract keywords
    insights = {}

    for keyword in keywords:
        try:
            page = wiki_wiki.page(keyword)
            insights[keyword] = page.summary[:200] if page.exists() else "No insight found."
        except Exception:
            insights[keyword] = "No insight found."

    return insights

# Example usage
note = "Machine learning is a subset of artificial intelligence."
print("Insights:", generate_insights(note))
