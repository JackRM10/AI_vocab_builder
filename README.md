# AI_vocab_builder

AI_vocab_builder is a Flask and spaCy web application designed to help users build vocabulary through active sentence practice.

The app presents a vocabulary word and definition, asks the user to write an original sentence using that word, then evaluates whether the word appears to be used correctly. The goal is to create a learning loop where users absorb a definition, apply it in writing, and receive feedback.

## Project Goals

* Build a working Flask web application
* Use spaCy to analyze user-submitted sentences
* Store vocabulary words in a CSV file
* Give feedback on word usage
* Provide example sentences and related-word suggestions
* Track user progress in a later phase

## Current MVP Scope

The first version will focus on:

* Loading words from `data/words.csv`
* Displaying one word and definition at a time
* Accepting a user-written sentence
* Checking whether the target word appears in the sentence
* Using spaCy for lemma and part-of-speech analysis
* Showing feedback to the user
* Logging attempts to a CSV file

## Planned Features

Future improvements may include:

* User accounts
* Personal progress tracking
* Practice history
* Difficulty levels
* Streaks and review sessions
* More detailed AI-style feedback
* Deployment to a public web URL

## Tech Stack

* Python
* Flask
* spaCy
* pandas
* HTML
* CSS
* CSV data storage

## Project Structure

```text
AI_vocab_builder/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── words.csv
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

## Data Format

The vocabulary list will be stored in `data/words.csv`.

Expected columns:

```csv
word,definition,pos,examples
```

Example:

```csv
detrimental,"tending to cause harm",ADJ,"The policy had a detrimental effect on the project."
```

## Local Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

Run the app:

```powershell
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Development Status

This project is currently in the MVP build phase.

Current focus:

1. Set up the Flask project structure
2. Add a minimal Flask route
3. Render an HTML template
4. Load vocabulary from CSV
5. Add spaCy sentence evaluation
6. Improve feedback and examples
