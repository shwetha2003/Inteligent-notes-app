from spellchecker import SpellChecker

def check_spelling(text):
    spell = SpellChecker()
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)

# Example usage
note = "Ths is a note with speling erors."
print("Corrected Text:", check_spelling(note))
