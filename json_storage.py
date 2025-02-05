# modules/json_storage.py
import json
import os
from datetime import datetime

# Path to the JSON file
JSON_PATH = os.path.join("data", "notes.json")

def init_json():
    """
    Initialize the JSON file if it doesn't exist.
    Creates an empty list as the default structure.
    """
    os.makedirs("data", exist_ok=True)  # Create the 'data' directory if it doesn't exist
    if not os.path.exists(JSON_PATH):
        with open(JSON_PATH, "w") as f:
            json.dump([], f)  # Initialize the file with an empty list

def save_note(title, content):
    """
    Save a note to the JSON file.
    :param title: Title of the note.
    :param content: Content of the note.
    """
    init_json()  # Ensure the JSON file exists
    note = {
        "title": title,
        "content": content,
        "created_at": datetime.now().isoformat()  # Add a timestamp
    }
    with open(JSON_PATH, "r+") as f:
        notes = json.load(f)  # Load existing notes
        notes.append(note)  # Add the new note
        f.seek(0)  # Move the file pointer to the beginning
        json.dump(notes, f, indent=4)  # Write the updated notes back to the file
        f.truncate()  # Remove any leftover data

def get_notes():
    """
    Retrieve all notes from the JSON file.
    :return: List of notes (dictionaries).
    """
    init_json()  # Ensure the JSON file exists
    with open(JSON_PATH, "r") as f:
        return json.load(f)  # Load and return the notes

# Initialize the JSON file when this module is imported
init_json()