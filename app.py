from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200579690"})  

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    # Extract intent name from Dialogflow request
    intent_name = req.get("queryResult").get("intent").get("displayName")

    if intent_name == "Check Weather":
        response_text = "The weather today is rainy and 15°C."  

    else:
        response_text = "I'm not sure how to respond to that."

    return jsonify({"fulfillmentText": response_text})

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
