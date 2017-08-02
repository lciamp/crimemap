import dateparser, datetime, json, string
from dbhelper import DBHelper
from flask import Flask, render_template, request

app = Flask(__name__)
DB = DBHelper()
categories = ['Mugging', 'Break-in', 'Robbery', 'Shooting']

# index
@app.route("/")
def home(error_message=None):
    crimes = DB.get_all_crimes()
    crimes = json.dumps(crimes)
    return render_template("home.html", crimes=crimes, 
                                        categories=categories,
                                        error_message=error_message)

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
    try:
        category = request.form.get('category')
        if category not in categories:
            return home()
        date = request.form.get('date')
        if not date:
            return home("Invalid date. Please use yyyy-mm-dd format.")
        try:
            latitude = float(request.form.get('latitude'))
            longitude = float(request.form.get('longitude'))
        except ValueError:
            return home()
        description = sanitize_string(request.form.get('description'))
        DB.add_crime(category, date, latitude, longitude, description)
    except Exception as e:
        print e
    return home()

# run the app
if __name__ == '__main__':
    app.run(port=5000, debug=True)

# HELPER FUNCTIONS
# function for formating the date if input by user 
def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.strftime(date, "%Y-%m-%d")
    except TypeError:
        return None

# function for sanitizing description text
def sanitize_string(userinput):
    whitelist = string.letters + string.numbers + " !?$.,;:-'()&"
    return filter(lambda x: x in whitelist, userinput)








