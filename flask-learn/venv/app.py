from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/home.html')

if __name__ == '__main__':
    sys.stderr = open('server.log', 'w')
    app.run(debug=True)