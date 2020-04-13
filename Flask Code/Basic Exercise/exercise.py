from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    name = request.args.get('username')
    lower_letter = any(c.islower() for c in name)
    upper_letter = any(c.isupper() for c in name)
    num_end = name[-1].isdigit()
    report = lower_letter and upper_letter and num_end

    return render_template('report.html', name=name, lower_letter=lower_letter, upper_letter=upper_letter, num_end=num_end, report=report)


if __name__ == '__main__':
    app.run(debug=True)