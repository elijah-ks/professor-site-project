from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage
users = {}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Store user in the dictionary
        users[username] = {"email": email, "password": password}
        return redirect(url_for("login"))

    return render_template("sign_up_page.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            return "Welcome, " + username + "!"
        return "Invalid credentials. Please try again."

    return render_template("index.html")
