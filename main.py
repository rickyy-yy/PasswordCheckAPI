from flask import Flask, request, jsonify
import os

app = Flask(__name__)

with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    common_passwords = f.read().splitlines()

@app.route("/check-password/<password>", methods=['GET'])
def check_password(password):
    length_flag = "Good"
    uppercase_flag = "Good"
    lowercase_flag = "Good"
    digit_flag = "Good"
    char_flag = "Good"
    common_password_flag = "Good"
    advice = []

    if len(password) < 8:
        length_flag = "Bad"
        advice.append("Password should be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        uppercase_flag = "Bad"
        advice.append("Password should contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        lowercase_flag = "Bad"
        advice.append("Password should contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        digit_flag = "Bad"
        advice.append("Password should contain at least one digit.")
    if not any(not char.isalnum() for char in password):
        char_flag = "Bad"
        advice.append("Password should contain at least one special character.")
    if password in common_passwords:
        common_password_flag = "Bad"
        advice.append("Password is too common. Consider using a more unique password.")
    

    body = {
        "Length": length_flag,
        "Uppercase": uppercase_flag,
        "Lowercase": lowercase_flag,
        "Digit": digit_flag,
        "Special Character": char_flag,
        "Common Password": common_password_flag,
        "Advice": advice
    }

    return jsonify(body), 200

if __name__ == '__main__':
    app.run(debug=True)