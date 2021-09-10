from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/about_me.html")
def about_me():
    return render_template("about_me.html")

@app.route("/projects.html")
def projects():
    return render_template("projects.html")

@app.route("/awards.html")
def awards():
    return render_template("awards.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    run()
