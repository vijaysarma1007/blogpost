from flask import Flask, render_template, request
import requests
import smtplib

EMAIL = "dtest2931@gmail.com"
PASSWORD = "informationun35"
app = Flask(__name__)
all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
background_image_url = 'https://images.unsplash.com/photo-1470092306007-055b6797ca72?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80'
@app.route('/')
def home():
    return render_template("index.html", image=background_image_url, posts=all_posts)

@app.route('/index')
def index():
    return render_template("index.html", image=background_image_url, posts=all_posts)

@app.route('/post/<int:index>')
def blog_posts(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == int(index):
            requested_post = all_posts[index-1]
    return render_template("post.html", image=background_image_url, post=requested_post)

@app.route('/about')
def about():
    return render_template("about.html", image=background_image_url)

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        textarea = request.form["textarea"]
        send_email(name, email, phone, textarea)
    return render_template("contact.html", image=background_image_url)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nname:{name}\nemail:{email}\nphone:{phone}\ntext message:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="svmsarma52@gmail.com", msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)
