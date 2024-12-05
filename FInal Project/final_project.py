from flask import Flask, jsonify, request, render_template

app= Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html",message="AnimeHub")

if __name__=="__main__":
    app.run(debug=True)
    