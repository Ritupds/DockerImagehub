from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi! Welcome to the Flask appplication."

if __name__ == '__main__':
    app.run(debug=True)