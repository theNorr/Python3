import os #imports os from the standard python library.
from flask import Flask, render_template #Import flask-class from PythonPackage & renders template from flask.

app = Flask(__name__) #creates an instance of flask and stores it in a variable app.

"""
Since we're just using a single module, we can use __name__
which is a built-in Python variable. Flask needs this so that it knows where to look for templates and static files.

"""


"""
the app.route decorator. In Python, a decorator starts with the @ sign, which is
also called pie notation. And, effectively, a decorator
is a way of wrapping functions.
when we try to browse to the root directory as indicated by the "/", then
flask triggers the index function underneath and returns the "Hello, World"
"""

@app.route('/') #route decorator to tell Flask what URL should trigger the following function.
def hello(): #the function.
    return render_template("index.html") #returns a template that's located inside the folder templates.

if __name__ == '__main__':  #compare __name__ to __main__. main is the default module in python.
    app.run(host=os.environ.get('IP'),  #run the app with argument: host is going to be the IP which is retrived by the os-function environ.get, from the enviroment in which we are running our app.
            port=int(os.environ.get('PORT')), #This does the same as above but it converts it to an int.
            debug=True) #helps us debug our code easier...Remove before deploy or submit.