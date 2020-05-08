import json

def json_load():
    with open("flashcards_db.json", "r", encoding="utf8") as f:
        return json.load(f)

def save_db():
    with open("flashcards_db.json", "w", encoding="utf8") as f:
        return json.dump(db, f)

        
db = json_load()


    

