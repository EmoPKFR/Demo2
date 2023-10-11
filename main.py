from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    if request.method == "POST":
        product_size = request.form.get("product_size")
        return redirect(url_for("about", size=product_size))
    

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        product_size = request.form.get("product_size")
        return redirect(url_for("about", size=product_size))
        
    return render_template("home.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    size = request.args.get("size")
    return render_template("about.html", size=size)

if __name__ == "__main__":
    app.run(debug=True)