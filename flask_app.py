from flask import Flask, render_template, jsonify, request
import src.web_controller as wc 
from src.exceptions import ValidationError
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

@app.route('/vector/encode/', methods = ["POST"])
def vector_encode():
   body = request.get_json()
   encoded, error_vector, error_count = wc.handle_encode(body)
   return jsonify({"encoded": encoded, "error_vector": error_vector, "error_count": error_count})

@app.route('/vector/send/', methods = ["POST"])
def vector_send():
   body = request.get_json()
   received, decoded = wc.handle_send(body)
   return jsonify({"received": received, "decoded": decoded,})

@app.route('/text')
def text():
    return render_template('text.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.errorhandler(ValidationError)
def handle_invalid_usage(error: ValidationError):
    response = jsonify({"error": error.message})
    response.status_code = 417
    return response

if __name__ == "__main__":
   import os

   port = int(os.environ.get('PORT', 5000))
   app.run(host="0.0.0.0", port=port, debug=True)