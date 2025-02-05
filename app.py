import streamlit as st
import torch

from summarization import summarize_text
from keyword_extraction import extract_keywords
from sentiment_analysis import analyze_sentiment
from auto_tagging import auto_tag
from entity_recognition import extract_entities
from insight_generation import generate_insights

def main():
    st.title("Intelligent Notes Processor")
    note = st.text_area("Enter your note:")
    if st.button("Process"):
        st.write("Summary:", summarize_text(note))
        st.write("Keywords:", extract_keywords(note))
        st.write("Sentiment:", analyze_sentiment(note))
        st.write("Tags:", auto_tag(note))
        st.write("Entities:", extract_entities(note))
        st.write("Insights:", generate_insights(note))

if __name__ == "__main__":
    main()
