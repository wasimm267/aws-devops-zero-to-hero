from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! This Is Wasim'

if __name__ == '__main__':
    app.run()




