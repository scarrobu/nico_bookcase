from flask import Flask, render_template, request, redirect, url_for
import sqlite3, json

app = Flask(__name__)

with open("slovnik.json", encoding='utf-8') as f:
    book_links = json.load(f)

@app.route("/")
def base():
    return render_template('base.jinja')

@app.route("/book/<book_title>", methods=['GET', 'POST'])
def book_detail(book_title):
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        
        conn = sqlite3.connect('knihy.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO reservations (user_name, book_title) VALUES (?, ?)", (user_name, book_title))
        conn.commit()

        conn.close()


        return redirect(url_for('book_list', ))
    return render_template('book_detail.jinja', book_title=book_title, book_links=book_links)

@app.route("/books")
def book_list():
    conn = sqlite3.connect('knihy.db')
    cursor = conn.cursor()

    cursor.execute("SELECT book_title, user_name FROM reservations")
    reservations = {row[0]: row[1] for row in cursor.fetchall()}

    conn.close()

    return render_template('books.jinja', reservations=reservations)

if __name__ == "__main__":
    app.run(debug=True)