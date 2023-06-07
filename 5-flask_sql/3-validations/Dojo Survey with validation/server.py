from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit_survey():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    return redirect("/result")

@app.route('/result')
def result():
    return render_template(
        "result.html", 
        name = session['name'],
        location = session['location'],
        fav_language = session['fav_language'],
        comment = session['comment']
        )


if __name__ == "__main__":
    app.run(debug=True)
