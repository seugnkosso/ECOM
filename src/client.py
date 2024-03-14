from flask import Flask, render_template, redirect

app = Flask(__name__)

app.config.from_pyfile("../config.py")

@app.route('/client/home')
def home_client():
    produits = [1,2,3,4]
    return render_template('client/home.html',prods=produits)

@app.route('/client/articles/<int:id_product>')
def product(id_product):
    if id_product == none:
        return redirect(url_for("home_client"))
    return render_template('client/product.html',prod = id_product)