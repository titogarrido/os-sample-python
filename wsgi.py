from flask import Flask
application = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    application.run()
