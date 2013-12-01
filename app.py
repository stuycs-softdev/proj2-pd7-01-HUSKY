from flask import Flask, render_template, url_for, request, redirect
import api

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
            if request.method == "GET":
                d = cbassfunc_to_return_only_original_list
                return render_template("convert.html", d=d, link=link, m="o")
            else:
                if request.form['button'] == "Descriptive":
                    d = cbassfun_to_return_Descriptive_list
                    return render_template("convert.html", d=d, link=link, m="d")
                elif request.form['button'] == "original":
                    d = cbassfunc_for only original
                    return render_template("convert.html", d=d, link=link, m="o")
                else:
                    d = cbassfunc_to_return_both_notations
                    return render_template("convert.html", d=d, link=link, m="b")
        else:
            return render_template("noconvert.html", url=link)
    except:
        return redirect(url_for('home'))

def checklink(link):
    d = api.findNot(link)
    return len(0) != 0

if __name__ == "__main__":
    app.debug = True
    app.run()
