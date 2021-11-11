from flask import Flask, redirect, url_for, render_template

app = Flask (__name__)

@app.route("/")
def Home():
    return render_template("homepage.html", content="home")

if __name__ == "__main__":
    app.run(debug=True)
