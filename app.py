from flask import Flask, render_template, url_for, request, redirect
import api
import converter

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        convert(request.form["url"])

@app.route('/converter/<link>', methods = ['GET', 'POST'])
def convert(link):
    try:
        if checklink(link):
            a = api.findNotation(link)
            d = convertNotation(a)
            if request.method == "GET":
                return render_template("convert.html", d=d, link=link, m="o", a=a)
            else:
                if request.form['button'] == "Descriptive":
                    return render_template("convert.html", d=d, link=link, m="d", a=a)
                elif request.form['button'] == "original":
                    return render_template("convert.html", d=d, link=link, m="o", a=a)
                else:
                    return render_template("convert.html", d=d, link=link, m="b", a=a)
        else:
            return render_template("noconvert.html", url=link)
    except:
        return redirect(url_for('home'))

def checklink(link):
    a = api.findNotation(link)
    return len(a) != 0

if __name__ == "__main__":
    app.debug = True
    app.run()
