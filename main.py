import pandas as pd
from flask import Flask, render_template


df = pd.read_csv("dictionary.csv")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/v1/<word>/')
def api(word):
    if word in df["word"].values:
        return {"word": word,
                "definitions": df.loc[df["word"] == word]["definition"].tolist()}
    else:
        return {"error": "word not found"}, 404

app.run(debug=True)