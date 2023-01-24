from flask import Flask, render_template
import requests

CONTENT_API = 'https://api.npoint.io/33ec397d16be22f81da9'

data = requests.get(CONTENT_API)

app = Flask(__name__)

@app.route('/')
def home():
    data = requests.get(CONTENT_API)
    return render_template("index.html", blog=data.json())

#
@app.route(f'/post/<int:index>')
def post(index):
    post = None
    for x in data.json():
        if x["id"] == index:
            post = x
    return render_template("post.html", butu=post)



if __name__ == "__main__":
    app.run(debug=True)
