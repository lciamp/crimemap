import json
from dbhelper import DBHelper
from flask import Flask, render_template, request

app = Flask(__name__)
DB = DBHelper()

# index
@app.route("/")
def home():
    try:
        crimes = DB.get_all_crimes()
        crimes = json.dumps(crimes)
    except Exception as e:
        print e
        crimes = None
    return render_template("home.html", crimes=crimes)

# add to database
@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("userinput")
        DB.add_input(data)
    except Exception as e:
        print e
    return home()

# clear database
@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print e
    return home()

@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get('category')
    date = request.form.get('date')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    description = request.form.get('description')
    try:
        DB.add_crime(category, date, latitude, longitude, description)
    except Exception as e:
        print e
    return home()



if __name__ == '__main__':
    app.run(port=5000, debug=True)

















