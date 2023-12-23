from flask import Flask, jsonify, request
from pda_controller import PDAController
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

valid_PDA:bool = False

@app.route('/PDA', methods=['GET'])
@cross_origin()
def is_valid_string():
    global valid_PDA
    data = {
        'valid': valid_PDA
    }
    return jsonify(data)

@app.route('/PDA', methods=['POST'])
@cross_origin()
def handle_data():
    global valid_PDA
    pda_controller = PDAController()
    # projectpath = request.form['projectFilepath']
    # print("nice")
    # your code
    # print(request.form)
    # print(request.get_json(force=True))
    clean_data: dict[str, list[str]] = pda_controller.handle_data(request.form)
    valid_PDA = pda_controller.init_pda(clean_data)
    print(valid_PDA)
    response = app.response_class(
        status=200
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
