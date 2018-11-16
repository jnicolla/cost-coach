from flask import Flask, jsonify, request
from flask_cors import CORS
from src.process_data import script_calc

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

def ret_app():
    return app

@app.route('/')
def index():
    '''
    Shows the server is up and running
    @ https://costcoachserver.herokuapp.com
    Will eventually want to reroute to Costcoach site
    but leave for testing purposes
    '''
    return '<h1>Hello world!</h1>'

@app.route('/calculate', methods=['POST'])
def calculate():
    input = request.get_json()
    # res = script_calc(answers.get('insurance'),answers.get('outOfPocket'),answers.get('copay'),answers.get('diagnosis'),answers.get('medications'))
    res = script_calc(input.get('insurance'), input.get('diagnosis'), input.get('medications'))
    response = { 'data':res }
    return jsonify(response)

'''
@Stefani
As you can see below, the data returned should be strings delimited by semi-colons.
Do as much as you can to clean the data before sending the response
and we'll collaborate to make it work with the frontend

@app.route('/test', methods=['POST'])
def test():
    data = [
        "Visit 1:Doctor Consultation;January 1, 2019;$100",
        "Visit 2:Chemotherapy Session;Febraury 2, 2019;$35",
        "Visit 3:Pharmacy Visit;March 3, 2019;$0"
        ]
    return jsonify({'events':data})
'''

if __name__=='__main__':
    app.run()