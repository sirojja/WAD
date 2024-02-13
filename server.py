from flask import Flask, render_template, current_app
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/static/<string:name>')
def send_static(name):
    return current_app.send_static_file(name)

if __name__ == '__main__':
    app.run(port = 5001)