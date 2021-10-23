from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "This page will be a homepage for users to signup and login."

@app.route('/feed/')
def get_students():
    return "This page will display users' feed."

@app.route('/profile/<int:username>/')
def get_students(username):
    return f"This page will display {username}'s' profile and their previously asked questions."

@app.route('/unanswered_question/')
def get_students():
    return "This page will display users' unanswered questions."

@app.route('/ask_a_question/')
def get_students():
    return "This page will allow users to submit a question to the site."

if __name__ == '__main__':
    app.run(debug=True)