from flask import Flask
app = Flask(__name__)

#static routing
@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route("/about")
def about():
    return '<h1>About Page</h1>'

# dynamic routes

@app.route('/puppy/<name>')
def puppy(name):
    return '<h1>This is a page for {}</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)

