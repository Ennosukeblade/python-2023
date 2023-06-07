from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route('/')
def author_page():
    return redirect('/authors/')

@app.route('/authors/')
def show_authors():
    all_authors = Author.get_all_authors()
    return render_template('authors.html', authors = all_authors)

@app.route('/author/create', methods=['POST'])
def create():
    Author.add_author(request.form)
    return redirect('/authors')

@app.route('/authors/<int:id>/')
def show_author_by_id(id):
    #author = Author.get_author_by_id({'id': id})
    author_with_fav_books = Author.get_fav_books({'id': id})
    not_fav_books = Book.not_fav_books({'id': id})

    return render_template('author_show.html', 
                           author_with_fav_books = author_with_fav_books, 
                           books = not_fav_books)

@app.route('/add_author_to_fav', methods=['POST'])
def add_author_fav():
    Author.add_author_to_fav(request.form)
    return redirect(f"/books/{request.form['book_id']}")

