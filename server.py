from flask import Flask, render_template, url_for, request, send_from_directory, session, jsonify
from opentok import OpenTok

app = Flask(__name__)

app.config['SECRET_KEY'] = b'dE\xad2g\x0c\x8d\xb9\x1cq\x86\x04:\xa8>\xc7\xc5\xc2Dr\xe7f\xf9\xeb'
# Replace with your OpenTok API key:
api_key = "46222472"
# Replace with your OpenTok API secret:
api_secret = "5cc7adf86081eae0abaf5a6cf43825a89f9f1990"
# Replace with the representative URL of your session:
session_address = '192.0.43.10'


@app.route('/publisher', methods=['GET'])
def loggedinUser():
    opentok_sdk = OpenTok(api_key, api_secret)
    session = opentok_sdk.create_session(session_address)
    token = opentok_sdk.generate_token(session.session_id)
    print("My token",token,"Session",session.session_id)
    return jsonify(token,session.session_id)

# Server Run on a port 5050
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5050 )