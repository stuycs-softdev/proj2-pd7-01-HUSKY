from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    
#@app.route('/moves/<link>', methods = ['GET', 'POST'])
#def moves(link):

if __name__ == "__main__":
    app.debug = True
    app.run()
