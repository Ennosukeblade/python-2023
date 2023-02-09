from flask import Flask, render_template
import math
app = Flask(__name__)

@app.route('/')
def check_board_8by8():
    return render_template("checkboard.html", row_num = 4, col_num = 4)

@app.route('/<int:num>')
def check_board(num):
    int_num = math.floor(num/2)
    return render_template("checkboard.html", row_num = int_num, col_num = 4)

@app.route('/<int:rownum>/<int:colnum>')
def check_board_dynamic(rownum, colnum):
    int_row_num = math.floor(rownum/2)
    int_col_num = math.floor(colnum/2)
    return render_template("checkboard.html", row_num = int_row_num, col_num = int_col_num)

if __name__=="__main__":
    app.run(debug=True)