from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    version = sys.version
    return render_template('hello.html', name=name, version=version)

if __name__ == "__main__":
    app.run()
