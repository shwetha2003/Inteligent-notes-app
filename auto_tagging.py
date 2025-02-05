def auto_tag(note):
    tags = []
    categories = {
        "Work": ["meeting", "deadline", "project"],
        "Personal": ["family", "friends", "holiday"],
        "Ideas": ["idea", "brainstorm", "innovation"]
    }
    for tag, keywords in categories.items():
        if any(keyword in note.lower() for keyword in keywords):
            tags.append(tag)
    return tags if tags else ["Uncategorized"]

# Example usage
note = "We need to brainstorm new ideas for the project."
print("Tags:", auto_tag(note))
