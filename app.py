
from flask import Flask, render_template

app = Flask(__name__)

# 首頁
@app.route('/')
def index():
    return render_template('index.html', title='讀書計畫首頁')

# 各分頁路由
@app.route('/competition')
def competition():
    return render_template('competition.html', title='競賽經驗')

@app.route('/activities')
def activities():
    return render_template('activities.html', title='課外活動')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html', title='幹部經驗')

@app.route('/club')
def club():
    return render_template('club.html', title='社團經驗')

@app.route('/electives')
def electives():
    return render_template('electives.html', title='多元選修課程')

@app.route('/ai')
def ai():
    return render_template('ai.html', title='AI應用')

if __name__ == '__main__':
    app.run(debug=True)