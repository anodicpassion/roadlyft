from flask import Flask, request, jsonify
import re
from flask_cors import CORS


app = Flask(__name__)
CORS(app, supports_credentials=True)


def is_valid_email(email):
    # Simple regex for validating an email
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


@app.route('/cnt-frm-luch-web', methods=['POST'])
def handle_form_submission():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or len(name) < 2:
        print("1")
        return jsonify({"status": "failure", "message": "Invalid name"}), 400

    if not email or not is_valid_email(email):
        print("2")
        return jsonify({"status": "failure", "message": "Invalid email"}), 400

    print(f"Received submission: Name={name}, Email={email}, Message={message}")
    print("3")
    url = f"""https://api.telegram.org/bot{api_key}/sendMessage?chat_id={5253099508}&text={"Hello Abhishek, I'm " + name + " here to inquire about your service. My phone number is " + phone + " and my location is " + location + "."}"""
    requests.post(url)
    return jsonify({"status": "success", "message": "Data received successfully"})


if __name__ == '__main__':
    app.run(debug=True, port=5550)
