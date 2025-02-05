from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import os

def create_search_index(notes):
    schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), note_id=ID(stored=True))
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
    ix = create_in("indexdir", schema)
    writer = ix.writer()
    for i, note in enumerate(notes):
        writer.add_document(title=f"Note {i}", content=note, note_id=str(i))
    writer.commit()

def search_notes(query):
    from whoosh.qparser import QueryParser
    ix = open_dir("indexdir")
    with ix.searcher() as searcher:
        query_parser = QueryParser("content", ix.schema)
        query = query_parser.parse(query)
        results = searcher.search(query)
        return [hit['content'] for hit in results]

# Example usage
notes = ["First note text.", "Second note text."]
create_search_index(notes)
print("Search Results:", search_notes("first"))
