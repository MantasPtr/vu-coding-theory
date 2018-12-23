from flask import Flask, render_template
app = Flask(__name__, static_folder='web', template_folder='web')

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/vector')
def vector():
    return render_template('vector.html')

@app.route('/text')
def text():
    return render_template('text.html')

@app.route('/image')
def image():
    return render_template('image.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)