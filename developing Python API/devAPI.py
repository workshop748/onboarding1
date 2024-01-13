from flask import Flask

app = Flask(__name__)


#creating a root
@app.route("/")
def home():
    return "this is home base"
@app.route("/getReposts")
def getReposts():
    return "100 reposts"
@app.route("/getLikes")
def getLikes():
    return "200 likes"
@app.route("/getBookmarks")
def getBookmarks():
    return "300 bookmarks"
if __name__== "__main__":
    app.run(debug=True)
