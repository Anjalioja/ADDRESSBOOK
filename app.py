from flask import Flask, render_template, request, redirect, url_for
import bookdb

app = Flask(__name__)

bookdb.init_db()


@app.route("/")
def index():
    contacts = bookdb.get_all_contacts()
    return render_template("index.html", contacts=contacts)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    address = request.form["address"]
   

    bookdb.add_contact(name, phone, email, address)
    return redirect(url_for("index"))


@app.route("/update/<int:cid>", methods=["POST"])
def update(cid):
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    address = request.form["address"]
    
    bookdb.update_contact(cid, name, phone, email, address)
    return redirect(url_for("index"))


@app.route("/delete/<int:cid>")
def delete(cid):
    bookdb.delete_contact(cid)
    return redirect(url_for("index"))


@app.route("/search")
def search():
    q = request.args.get("q", "")
    results = bookdb.search_contacts(q)
    return render_template("index.html", contacts=results, search_query=q)


if __name__ == "__main__":
    app.run(debug=True)
