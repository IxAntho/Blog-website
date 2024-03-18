from flask import Flask, render_template
import requests
from datetime import date

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

POST_BACKGROUND = ["https://images.unsplash.com/photo-1516481605912-d34c1411504c?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGNhY3R1c3xlbnwwfHwwfHx8MA%3D%3D", "https://images.unsplash.com/photo-1449358070958-884ac9579399?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDN8fGFjdGl2aXR5fGVufDB8fDB8fHww", "https://images.unsplash.com/photo-1444459094717-a39f1e3e0903?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTI4fHxudXRyaXRpb258ZW58MHx8MHx8fDA%3D"]

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
    bg = POST_BACKGROUND[post_id-1]
    return render_template("post.html", post=content, background=bg)


if __name__ == "__main__":
    app.run(debug=True)
