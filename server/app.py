from flask import Flask, jsonify, request
from flask_cors import CORS
from dummy import dummy_calc # replace this line/method with the provided algo

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    answers = request.get_json()
    res = dummy_calc(answers.get('insurance'),answers.get('outOfPocket'),answers.get('copay'),answers.get('diagnosis'),answers.get('medications'))
    #cost = dummy_cost(answers.get('insurance'),answers.get('outOfPocket'),answers.get('copay'),answers.get('diagnosis'),answers.get('medications'))
    response = { 'html':res[0], 'cost':res[1]}
    return jsonify(response)


if __name__=='__main__':
    app.run()