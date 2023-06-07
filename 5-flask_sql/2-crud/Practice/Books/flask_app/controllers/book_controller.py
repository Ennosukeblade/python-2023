from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route('/books')
def all_books():
    all_books = Book.get_all_books()
    return render_template("books.html", all_books = all_books)

@app.route('/add_books_to_fav', methods=['POST'])
def add_to_fav():
    Book.add_books_to_fav(request.form)
    return redirect(f"/authors/{request.form['author_id']}")

@app.route('/books/add', methods=['POST'])
def add_book():
    Book.add_book(request.form)
    return redirect("/books")

@app.route('/books/<int:id>')
def book_by_id(id):
    # book = Book.get_book_by_id({'id':id})
    book = Book.get_favorited_by_authors({'id':id})
    authors = Author.not_favorited_by_authors({'id':id})
    return render_template("book_show.html", book = book, other_authors = authors)