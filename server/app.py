from flask import Flask, jsonify, request
from flask_cors import CORS
from src.process_data import script_calc # replace this line/method with the provided algo

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    answers = request.get_json()
    res = script_calc(answers.get('insurance'),answers.get('diagnosis'),answers.get('medications'))
    # res = script_calc('Duke Select', 'Prostate Cancer', 'Oral')
    response = { 'html':res[0], 'cost':res[1]}
    return jsonify(response)

'''
@Stefani
As you can see below, the data returned should be strings delimited by semi-colons.
Do as much as you can to clean the data before sending the response
and we'll collaborate to make it work with the frontend

The example of the output of the processing scrypt:
format: 'Visit, Catagory, OOPM'
['1, Lab, 1300', '2, Specialist, 400']

'''

@app.route('/test', methods=['POST'])
def test():
    data = [
        "Visit 1:Doctor Consultation;January 1, 2019;$100",
        "Visit 2:Chemotherapy Session;Febraury 2, 2019;$35",
        "Visit 3:Pharmacy Visit;March 3, 2019;$0"
        ]
    return jsonify({'events':data})


if __name__=='__main__':
    app.run()