from flask import Flask, render_template, url_for,flash,request
import requests
from bs4 import BeautifulSoup as BS
from parser1 import pars

# r = requests.get('https://www.avito.ru/')
# html = BS(r.content, 'html.parser')

# for el in html.select(".items > .article-summary"):
#     title = el.select('.caption > a')
#     print(title[0].text)


app = Flask(__name__)
app.config['SECRET_KEY'] = "22814881488askfhdlkajfsld"
@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/find')
# @app.route('/find/<string:product>')
@app.route('/find', methods=["POST","GET"])
def parser():
    if request.method == "POST":
        print(request.form["message"])
        flash('Все результаты по поиску: ' + request.form["message"])
        flash(pars(request.form["message"]))

    # return(str(pars(product)))
    return render_template("parser.html")




if __name__ == "__main__":
    app.run(debug=True)