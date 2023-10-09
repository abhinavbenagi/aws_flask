from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return render_template('message.html')  


if __name__ == "__main__":
    application.run(debug=True)
