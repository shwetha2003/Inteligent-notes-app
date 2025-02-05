import spacy

def extract_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = {ent.text: ent.label_ for ent in doc.ents}
    return entities

# Example usage
note = "Your note text goes here. Mention John Doe and New York."
print("Entities:", extract_entities(note))
