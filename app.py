from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template("home.html")
    elif request.method == 'POST':
        url_received = request.form['url_input']
        return url_received
    


if __name__ == '__main__':
    app.run(port=5000, debug=True)
