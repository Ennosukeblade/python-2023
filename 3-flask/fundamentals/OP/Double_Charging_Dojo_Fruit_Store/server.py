from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/checkout', methods=['POST'])
# def checkout():
#     print(request.form)
#     return render_template("checkout.html")


@app.route('/fruits')
def fruits():
    fruits = ["apple", "blackberry", "raspberry", "strawberry"]
    return render_template("fruits.html", fruits=fruits)


@app.route('/checkout', methods=['POST'])
def add_cart():
    data = request.form
    fruits_count = int(data['strawberry']) + \
        int(data['raspberry']) + int(data['apple'])

    print(f"Charging {data['first_name']} for {fruits_count} fruits")

    today = datetime.today().strftime("%B %d, %Y %I:%M:%S %p")
# after refreshing the form is resubmited and this isn't a good behavior because client can be charged another time accidently,
# we have to do a redirect after submission to avoid this behavior
    return render_template("checkout.html", data=data, count=fruits_count, date=today)


if __name__ == "__main__":
    app.run(debug=True)
