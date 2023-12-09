from flask import Flask, render_template
from graph import Graphs
from get_data import *

app = Flask(__name__)

username = 'Caio Madeira'

light_bills_year = get_bills_from_emails('LIGHT', bills)
clarobills = claro_MANUAL_VALUES
print("Light Bills year: ", light_bills_year)
print("Claro Bills year: ", clarobills)
@app.route("/")
def home():
    return render_template("index.html",
                           username=username, bills=light_bills_year, clarobills=clarobills)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
