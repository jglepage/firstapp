__project__ = 'flask'
#__name__ = 'jeffl'
__author__ = 'Jeff LePage'

from flask import Flask
app = Flask(__name__)
print __name__

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)

