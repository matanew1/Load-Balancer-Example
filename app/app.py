# app.py
from flask import Flask

app = Flask(__name__)

# Import and register the blueprint
from routes import bp as my_blueprint
app.register_blueprint(my_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
