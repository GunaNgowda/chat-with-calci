from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    action = req.get('queryResult').get('action')
    parameters = req.get('queryResult').get('parameters')
    
    if action == 'calculate':
        num1 = parameters.get('number1')
        num2 = parameters.get('number2')
        operation = parameters.get('operation')
        result = None
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        
        response = {
            'fulfillmentText': f'The result is {result}'
        }
    else:
        response = {
            'fulfillmentText': 'Sorry, I did not understand that operation.'
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
