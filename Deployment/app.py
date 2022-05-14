# Importing Libraries from Flask framework
from flask import Flask, render_template
from routes import bp1

# Creation of the Flask application that will be responsible for uploading the application to the Web.
app = Flask(__name__)

# Linking file routes.py to be able to access the backend route.
app.register_blueprint(bp1)

# Declaration of the main route that will call the home.html file as soon as the application is uploaded.


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=False)

# To run the program locally, just have Python installed.
# Install the dependencies, then open a CMD in the project folder
# and typing "python app.py", it will open a server at a given address
# in CMD.
