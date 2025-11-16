from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    user_input = request.form.get("user_input")

    print("User entered:", user_input)

    return redirect("/")


if __name__ == "__main__":

    app.run(debug=True)