from flask import Flask, render_template
app = Flask(__name__)

posts = [ {
        "title": "The Road Not Taken",
        "author": "Robert Frost",
        "text": "Two roads diverged in a yellow wood, And sorry I could not travel both..."
    },
    {
        "title": "Ozymandias",
        "author": "Percy Bysshe Shelley",
        "text": "I met a traveller from an antique land Who said: Two vast and trunkless legs of stone..."
    },
    {
        "title": "Daffodils",
        "author": "William Wordsworth",
        "text": "I wandered lonely as a cloud That floats on high o'er vales and hills..."
    },
    {
        "title": "Sonnet 18",
        "author": "William Shakespeare",
        "text": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate..."
    },
    {
        "title": "The Raven",
        "author": "Edgar Allan Poe",
        "text": "Once upon a midnight dreary, while I pondered, weak and weary..."
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about.html")
def about():
    return render_template("about.html"   )

if __name__ == '__main__':
    app.run(debug=True)