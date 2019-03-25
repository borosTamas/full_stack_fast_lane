from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def game():
    row_num = int(request.args.get('row-num', 30))
    col_num = int(request.args.get('col-num', 50))
    return render_template('game.html', row_num=row_num, col_num=col_num)


if __name__ == '__main__':
    app.run(debug=True)