from pathlib import Path

import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

DATA_FILE = Path(__file__).parent / "data" / "words.csv"


@app.route("/")
def home():
    words = pd.read_csv(DATA_FILE)

    first_word = words.iloc[0]

    return render_template(
        "index.html",
        word=first_word["word"],
        definition=first_word["definition"],
        pos=first_word["pos"],
    )


if __name__ == "__main__":
    app.run(debug=True)