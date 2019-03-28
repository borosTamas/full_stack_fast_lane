from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        colour = request.form.get('fav_colour')
        print(user_name, colour)
        return redirect('/game')
    return render_template('start.html')

@app.route('/game')
def game():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)