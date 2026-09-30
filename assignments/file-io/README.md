# 📘 Assignment: Reading and Writing JSON Files

## 🎯 Objective

Practice reading and writing structured data with Python's built-in `json` module. You will build a small reading log that keeps its entries after the program ends.

## 📝 Tasks

### 🛠️ Load and Display Reading Entries

#### Description
Use the provided starter code and `reading_log.json` file to load a list of reading entries and display each book's title and author.

#### Requirements
Completed program should:

- Read the JSON array from `reading_log.json` using Python's `json` module
- Display each entry's title and author
- Display a helpful message when the reading log contains no entries


### 🛠️ Add and Save a Reading Entry

#### Description
Ask the user for a book title and author, add that entry to the reading log, and save the updated list to the JSON file.

#### Requirements
Completed program should:

- Add the new title and author without removing existing entries
- Write the complete list back to `reading_log.json` as valid JSON
- Keep the saved entries available when the program is run again
- Format the JSON output so it is easy for a person to read