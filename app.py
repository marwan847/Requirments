from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        return render_template('page1.html',
                               submitted=True,
                               name=name,
                               email=email,
                               age=age)

    return render_template('page1.html')


if __name__ == '__main__':
    app.run(debug=True)
