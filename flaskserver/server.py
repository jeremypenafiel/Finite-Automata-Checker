from flask import Flask, jsonify, request
from pda_controller import PDAController
from flask_cors import CORS, cross_origin
# from waitress import serve


my_app = Flask(__name__)
cors = CORS(my_app)
my_app.config['CORS_HEADERS'] = 'Content-Type'

valid_PDA:bool = False

@my_app.route('/PDA', methods=['GET'])
@cross_origin()
def is_valid_string():
    print("hello")
    global valid_PDA
    data = {
        'valid': valid_PDA
    }
    return jsonify(data)

@my_app.route('/PDA', methods=['POST'])
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
    response = my_app.response_class(
        status=200
    )
    return response

# mode = "prod"

# if __name__ == '__main__':
#     if mode == "dev":
#         app.run(host='0.0.0.0', port=42069)
#     else:
#         serve(app, host='0.0.0.0', port=42069, threads=1)
