from flask import Flask, request, jsonify
from flask_mail import Mail, Message

sendmail = Flask(__name__)

# Mail configuration
sendmail.config['MAIL_SERVER'] = 'smtp.gmail.com'
sendmail.config['MAIL_PORT'] = 587
sendmail.config['MAIL_USE_TLS'] = True
sendmail.config['MAIL_USERNAME'] = 'arunaraje152005@gmail.com'
sendmail.config['MAIL_PASSWORD'] = 'kfxr eziw hptv quel'

mail = Mail(sendmail)

@sendmail.route("/sendingamail", methods=["Post","Get"])
def send_mail():
    data = request.json

    receiver = data["email"]
    message_text = data["message"]

    msg = Message(
        "First Flask",
        sender="arunaraje152005@gmail.com",
        recipients=["divyashreesenthilkumar@gmail.com"]
    )

    msg.body = message_text

    mail.send(msg)

    return jsonify({"message": "Mail Sent Successfully!"})

if __name__ == "__main__":
    sendmail.run(debug=True)