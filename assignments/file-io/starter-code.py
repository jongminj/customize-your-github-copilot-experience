import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("reading_log.json")


def load_entries(file_path=DATA_FILE):
    # Load the JSON array from file_path and return it.
    pass


def save_entries(entries, file_path=DATA_FILE):
    # Save entries to file_path as readable JSON.
    pass


def main():
    entries = load_entries()

    if entries:
        print("Reading log:")
        for entry in entries:
            print(f"- {entry['title']} by {entry['author']}")
    else:
        print("Your reading log is empty.")

    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    entries.append({"title": title, "author": author})
    save_entries(entries)
    print("Reading entry saved.")


if __name__ == "__main__":
    main()