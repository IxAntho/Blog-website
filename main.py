from flask import Flask, render_template
import requests
from datetime import date

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route("/")
def home_page():
    response = requests.get(url=BLOG_URL)
    all_posts = response.json()
    today = date.today()
    formatted_date = today.strftime("%B %d, %Y")
    print(all_posts)
    return render_template("index.html", posts=all_posts, current_date=formatted_date)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    response = requests.get(url=BLOG_URL)
    all_posts = response.json()
    content = all_posts[post_id-1]
    return render_template("post.html", post=content)


if __name__ == "__main__":
    app.run(debug=True)
