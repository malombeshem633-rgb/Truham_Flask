# importing flask to our application
from flask import *

# initializing the flask app
app = Flask(__name__)

# define a simple route/endpoint
# this route corresponds to a web application function
@app.route("/api/home")
# this is the function that runs when the route is accessed
def home():
    return jsonify({"Message":"Welcome to home api"})




# define a simple route
@app.route("/api/products")
# function corresponding to the route
def products():
    return jsonify({"message":"Welcome to products api"})


@app.route("/api/services")
def services():
    return jsonify({"Message":"Welcome to services api"})


# runs the app when this file is executed
app.run(debug = True)