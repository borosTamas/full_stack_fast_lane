from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def game():
    row_num = 100
    col_num = 50
    return render_template('game.html', row_num=row_num, col_num=col_num)


if __name__ == '__main__':
    app.run(debug=True)