from flask import Flask

app = Flask(__name__)


# Homepage
@app.route('/home/', methods=["PUT", "PATCH"])
def home_page():
    return "This page will be a homepage for users to signup and login."

    
# Feed page
@app.route('/feed/', methods=["GET"])
def feed():
    return "This page will display users' feed with latest answered questions."


# Users' profile page
@app.route('/profile/<string:username>/', methods=["GET"])
def profile(username):
    return f"This page will display {username}'s' profile and their previously asked questions."

@app.route('/profile/<string:username>/', methods=["Delete"])
def profile(username):
    return f"This page will display {username}'s' profile and let them delete their previously asked questions."

@app.route('/profile/<string:username>/', methods=["PUT", "PATCH"])
def profile(username):
    return f"This page will display {username}'s' profile and let them edit their previously asked questions."



# Edit profile page
@app.route('/profile/<string:username>/edit', methods=["PUT", "PATCH"])
def profile(username):
    return f"This page will display {username}'s' profile and let them edit their profile."



# Unanswered questions page
@app.route('/question/unanswered/', methods=["GET"])
def unanwsered_qs():
    return "This page will display users' unanswered questions."

@app.route('/question/unanswered/', methods=["POST"])
def unanwsered_qs():
    return "This page will allow for users to answer unanswered questions."


# Previously answered questions page
@app.route('/question/answered/', methods=["GET"])
def unanwsered_qs():
    return "This page will display any questions the current user has answered."

@app.route('/question/answered/', methods=["PUT", "PATCH"])
def unanwsered_qs():
    return "This will allow for users to edit their previous answers."

@app.route('/question/answered/', methods=["DELETE"])
def unanwsered_qs():
    return "This will allow for users to delete their previous answers."



# Submit question page
@app.route('/question/submit/', methods=["POST"])
def ask_a_qs():
    return "This page will allow users to submit a question to the site."

if __name__ == '__main__':
    app.run(debug=True)