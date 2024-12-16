from flask import Flask, render_template, request

from main import *
app = Flask(__name__)

bk = BurgerKing()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    order_data = request.form['order']
    order_lines = order_data.split("\r\n")
    user = 'user'
    order_items = []
    for line in order_lines:
        item, count = line.split(' x')
        order_items.append([item, int(count)])
    bk.new_order_from_user(user, order_items)
    combos = bk.genereate_combos()
    return render_template('order_result.html', combos=combos)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

