import json
import os

# Define the file path for the dictionary data
DATA_FILE = "dictionary_data.json"

def load_dictionary():
    """Loads the dictionary from the JSON file. If it doesn't exist, returns an empty dict."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Error loading dictionary file. Starting with an empty dictionary.")
        return {}

def save_dictionary(data):
    """Saves the dictionary to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("Dictionary saved locally!")
    except IOError:
        print("Error saving dictionary.")

# Load translations at start
translations = load_dictionary()

print("Welcome to the Ultimate Banglish Dictionary (/q to exit)!")
print("Type a word in Banglish to get its English meaning.")
print(f"Loaded {len(translations)} words from the dictionary.")

task = True
while task:
    try:
        Word = input("Enter the word: ").strip().lower()
    except EOFError:
        break

    if Word == "/q":
        task = False
        break

    if not Word:
        continue

    # Print translation
    if Word in translations:
        print(f"Translation: {translations[Word]}")
    else:
        print(f"Translation: Word '{Word}' not found in dictionary.")
        choice = input("Do you want to add it to your LOCAL dictionary? (y/n): ").strip().lower()
        if choice == 'y':
            translation = input("Enter the translation of your word: ").strip()
            if translation:
                translations[Word] = translation
                save_dictionary(translations)
                print(f"Added: {Word} -> {translation}")
            else:
                print("Translation cannot be empty.")
