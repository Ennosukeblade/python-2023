from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play_3_times():
    return render_template("index.html", times=3)

@app.route('/play/<int:x>')
def play_x_times(x):
    return render_template("index.html", x=x)

@app.route('/play/<int:x>/<color>')
def play_x_times_with_color(x, color):
    bg_color = f"style=background-color:{color}"
    return render_template("index.html", x=x, color=bg_color)

if __name__=="__main__":
    app.run(debug=True)