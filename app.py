from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('names.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS names (id INTEGER PRIMARY KEY, name TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        conn = sqlite3.connect('names.db')
        c = conn.cursor()
        c.execute('INSERT INTO names (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        return redirect('/')

    conn = sqlite3.connect('names.db')
    c = conn.cursor()
    c.execute('SELECT name FROM names')
    names = c.fetchall()
    conn.close()

    return render_template('index.html', names=names)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
