from flask import Flask, request, jsonify

app = Flask(__name__)

# List of emails with access to premium features
premium_users = ["d.vanbillemont@outlook.com", "user2@example.com", "user3@example.com"]

@app.route('/access', methods=['POST'])
def access():
    data = request.get_json()
    email = data.get('email')

    if email in premium_users:
        return jsonify({"message": "Access granted to premium features"}), 200
    else:
        return jsonify({"message": "Access denied"}), 403

if __name__ == '__main__':
    app.run(debug=True)