from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health_check():
    return {"status": "up"}

@app.route('/ping')
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(debug=True)

