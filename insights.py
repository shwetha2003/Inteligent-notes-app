import wikipediaapi


from modules.keyword_extraction import extract_keywords


def generate_insights(text):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    keywords = extract_keywords(text)  # Ensure extract_keywords() is available
    insights = {}

    for keyword in keywords:
        try:
            page = wiki_wiki.page(keyword)
            insights[keyword] = page.summary[:200] if page.exists() else "No insight found."
        except Exception:
            insights[keyword] = "No insight found."

    return insights
