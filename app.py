from flask import Flask, render_template
app = Flask(__name__)


@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "Contact information: 123 Main St., City, State, ZIP"

@app.route('/')
def home():
    return render_template('index.html', name='Flask')

if __name__ == '__main__':
    app.run(debug=True)