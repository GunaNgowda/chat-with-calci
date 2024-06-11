from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = process_request(req)
    return jsonify(res)

def process_request(req):
    result = req.get("queryResult")
    intent = result.get("intent").get("displayName")

    if intent == "Addition":
        num1 = float(result.get("parameters").get("number1"))
        num2 = float(result.get("parameters").get("number2"))
        return make_response(num1 + num2)

    elif intent == "Subtraction":
        num1 = float(result.get("parameters").get("number1"))
        num2 = float(result.get("parameters").get("number2"))
        return make_response(num1 - num2)

    elif intent == "Multiplication":
        num1 = float(result.get("parameters").get("number1"))
        num2 = float(result.get("parameters").get("number2"))
        return make_response(num1 * num2)

    elif intent == "Division":
        num1 = float(result.get("parameters").get("number1"))
        num2 = float(result.get("parameters").get("number2"))
        if num2 == 0:
            return {"fulfillmentText": "Error: Division by zero is not allowed."}
        return make_response(num1 / num2)

def make_response(result):
    return {
        "fulfillmentText": f"The result is {result}"
    }

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 8080)))
