from flask import Flask, request
from pda_controller import PDAController


app = Flask(__name__)
pda_controller = PDAController()

@app.route('/members')
def members():
    return {"members": ["member1", "member2", "member3"]}


@app.route('/PDA', methods=['POST'])
def handle_data():
    # projectpath = request.form['projectFilepath']
    print("nice")
    # your code
    print(request.form)
    pda_controller.handle_data(request.form)
    response = app.response_class(
        status=200
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
