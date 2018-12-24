from flask import Flask, render_template, jsonify, request
import src.web_controller as wc 

app = Flask(__name__, static_folder='web', template_folder='web')


@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/vector')
def vector():
    return render_template('vector.html')

@app.route('/vector/gen-matrix/', methods = ["POST"])
def vector_gen_matrix():
   body = request.get_json()
   gen_matrix_str = wc.handle_generate_matrix(body)
   return jsonify({"matrix": gen_matrix_str})


@app.route('/text')
def text():
    return render_template('text.html')

@app.route('/image')
def image():
    return render_template('image.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)