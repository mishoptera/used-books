from flask import render_template
from flask_app import app
from flask import request
from flask_app.a_Model import ModelIt
from flask_app.megastring import popularbrandsfunction


@app.route('/')
# # @app.route('/index')
# # def index():
# #     return render_template("index.html",
# #        title = 'Home', user = { 'nickname': 'Misha' },
# #        )
# @app.route('/input')
def usedbooks_input():
    return render_template("input.html")

@app.route('/output')
def usedbooks_output():
    condition_ordinal = request.args.get('condition')
    title = request.args.get('title')
    brand_name = request.args.get('brand_name')
    total_price = request.args.get('price')
    free_shipping = request.args.get('free_shipping')
    description = request.args.get('description')
    description_length = len(description)
    if len(brand_name) == 0:
        brand_included = 0
    else:
        brand_included = 1
    topbrands = popularbrandsfunction(brand_name, title, description)
    binary_result = ModelIt(condition_ordinal, total_price, free_shipping, brand_included, description_length, topbrands)
    if binary_result == 1:
        the_result = "Congratulations! Someone just might 'buy buy' your book."
        ideas = ''
    else:
        the_result = "Sorry, your book is unlikely to sell if you post it like this."
        if int(free_shipping) == 0:
            ideas = "To increase your chances of success, try making shipping free."
        elif int(brand_included) == 0:
            ideas = "To increase your chances of success, try including a brand label."
        elif int(condition_ordinal) > 1:
            ideas = "To increase your chances of success, see if you can improve the condition of your book."
        elif int(total_price) > 3:
            ideas = "To increase your chances of success, consider lowering the price of your book."
        else:
            ideas = "Consider donating or recyling it."
    return render_template("output.html", the_result = the_result, ideas = ideas)
