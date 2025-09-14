from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bmw", methods=["GET", "POST"])
def bmw():
    config = None
    if request.method == "POST":
        config = {
            "Модель": request.form.get("model"),
            "Цвет": request.form.get("color"),
            "Двигатель": request.form.get("engine")
        }
    return render_template("bmw.html", config=config)

@app.route("/mercedes", methods=["GET", "POST"])
def mercedes():
    config = None
    if request.method == "POST":
        config = {
            "Модель": request.form.get("model"),
            "Цвет": request.form.get("color"),
            "Двигатель": request.form.get("engine")
        }
    return render_template("mercedes.html", config=config)

@app.route("/compare")
def compare():
    return render_template("compare.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)