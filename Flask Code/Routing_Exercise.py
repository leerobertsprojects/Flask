# Set up your imports here!
# import ...
from flask import Flask
app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return '<h1>Goto /puppy_latin/name to find out your puppy latin name</h1>'
    # Welcome Page
    # Create a generic welcome page.

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    if name[-1] != 'y':
        return f'<h1>Your name is {name} but your puppy latin name is {name}y</h1>'
    else:
        latin_name = name[0:-1]
        return f'<h1>Your {name} is but your puppy latin name is {latin_name}iful</h1>'

    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"


if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
