from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        message = request.form.get("message")
        return render_template("contact.html", success=True, name=name, phone=phone, message=message)
    return render_template("contact.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)