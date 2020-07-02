import os  # imports os from the standard python library.
import json  # imports the json-library.
from flask import Flask, render_template, request, flash  # Import flask-class from PythonPackage & renders template from flask and also request library.

"""
to display a non-permanent message to the user, something that only stays until
we refresh the page or go to a different one.
"""

app = Flask(__name__)  # creates an instance of flask and stores it in a variable app.
app.secret_key = 'some_secret'

"""
Since we're just using a single module, we can use __name__
which is a built-in Python variable. Flask needs this so that it knows
where to look for templates and static files.
app.secret_key = A key needed by the flash message to sign the contact form message.
"""


"""
the app.route decorator. In Python, a decorator starts with the 'at'
sign, which is
also called pie notation. And, effectively, a decorator
is a way of wrapping functions.
when we try to browse to the root directory as indicated by the "/", then
flask triggers the index function underneath and returns the "Hello, World"
"""

@app.route('/')  # route decorator to tell Flask what URL should trigger the following function.
def index():  # the function which is matched in the menu list items in our html-files.
    return render_template("index.html")  # returns a template that's located inside the folder templates.


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:  # Opens the referensed file as json_data, and "r" for reading.
        data = json.load(json_data)  # Sets my data variable to the JSON parsed data that we've sent through
    return render_template("about.html", page_title="About", company=data)  # Then we pass that data into the return, called company.


@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    
    return render_template("member.html", member=member)


@app.route('/contact', methods=["GET", "POST"])  # the methods that are allowed are GET and POST.
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == '__main__':   # compare   __name__   to   __main__  . main is the defaultmodule in python.
    app.run(host=os.environ.get('IP'),   # run the app with argument: host is going to be the IP which is retrived by the os-function environ.get, from the enviroment in which we are running our app.
            port=int(os.environ.get('PORT')),  # This does the same as above but it converts it to an int.
            debug=True)  # helps us debug our code easier...Remove before deploy or submit.