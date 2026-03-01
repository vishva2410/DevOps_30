from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_devops():
    return "Hello, DevOps! This is a simple Flask app running in Docker."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
