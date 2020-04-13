from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Lee'
    letters = list(name)
    pup_dict = {'puppy':'pug','breed':'bulldog'}
    list1 = ['buster', 'spike', 'fluffy']
    return render_template('templates.html', name=name, letters=letters, pup_dict=pup_dict, list1=list1)


if __name__ == '__main__':
    app.run(debug=True)