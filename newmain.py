from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/headingparagraph')
def basic():
    return render_template('headpar.html')

@app.route('/fontstyle')
def font():
    return render_template('fontstyle.html')

@app.route('/list')
def lists():
    return render_template('list.html')

@app.route('/image')
def image():
    return render_template('image.html')

if __name__ == "__main__":
    app.run(debug=True)