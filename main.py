"""
Main file for the E2EE Toolkit. This file consists of
1. UI Code
2. Encryption and Decryption Modules
3. Diffie-Hellman Key Exchange Function
"""
from flask import Flask, app, render_template, request, redirect, url_for, jsonify
from session import Session


print("Starting app!")
app = Flask(__name__)
app.debug = True

chat_session = Session()


@app.route("/")
def deliver_homepage():
    print(app.instance_path)
    print("request reached")

    context = {
        "session": chat_session,
        "server_messages": chat_session.get_server_messages(),
        "user1_messages": chat_session.get_decrypted_messages_for_user("Alice"),
        "user2_messages": chat_session.get_decrypted_messages_for_user("Bob"),
        "user1_username": chat_session.user_1.name,
        "user2_username": chat_session.user_2.name,
        "sharedkey": str(chat_session.user_1.shared_secret),
        "user1_pub": str(chat_session.user_1.public_key),
        "user1_priv": str(chat_session.user_1.private_key),
        "user2_pub": str(chat_session.user_2.public_key),
        "user2_priv": str(chat_session.user_2.private_key),
    }

    return render_template("index.html", **context)


@app.route("/send/<username>", methods=["POST"])
def send_message(username):

    if request.method == "POST":
        username = username
        message = request.form["message"]
        print(f"sending {message} from {username}")

        chat_session.send_message_for_user(username, message)

        return redirect(url_for("deliver_homepage"))
