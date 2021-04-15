# Import Flask dependency.
from flask import Flask

# Create a new Flask instance.
app = Flask(__name__)

# Create a route - first define the root, then a function (route).
@app.route('/')
def hello_world():
    return 'Hello World!'

# Create a second route 
@app.route('/route_two/')
def test_one():
    return "Here's a second route to play with."