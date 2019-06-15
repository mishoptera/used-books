from flask import render_template
from flask_app import app
from flask import request
from flask_app.a_Model import ModelIt


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Misha' },
       )
@app.route('/input')
def usedbooks_input():
    return render_template("input.html")

@app.route('/output')
def usedbooks_output():
    condition_ordinal = request.args.get('condition')
    total_price = request.args.get('price')
    free_shipping = request.args.get('free_shipping')
    brand_included = request.args.get('brand')
    description = request.args.get('description')
    description_length = len(description)
    binary_result = ModelIt(condition_ordinal, total_price, free_shipping, brand_included, description_length)
    if binary_result == 1:
        the_result = "Congratulations! This should sell!"
    else:
        the_result = "Sorry, this probably won't sell as is."
    return render_template("output.html", the_result = the_result)
