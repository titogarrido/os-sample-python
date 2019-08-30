from flask import Flask, render_template
import sys

application = Flask(__name__)

@application.route('/')
@application.route('/<name>')
def hello(name=None):
    version = sys.version
    return render_template('hello.html', name=name, version=version)

if __name__ == "__main__":
    application.run()
