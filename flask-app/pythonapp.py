# Import flask module
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, DevOps!'

# main driver function
if __name__ == "__main__":
    app.run(host='0.0.0.0')
