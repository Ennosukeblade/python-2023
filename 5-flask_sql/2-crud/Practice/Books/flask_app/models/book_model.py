from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import author_model


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorited_by = []

    @classmethod
    def get_all_books(cls):
        query = """
                SELECT * from books;
                """
        results = connectToMySQL(DB).query_db(query)
        books = []
        for row in results:
            books.append(cls(row))
        return (books)

    @classmethod
    def add_book(cls, data):
        query = """
                INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s)
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_book_by_id(cls, data):
        query = """
                SELECT * from books WHERE id = %(id)s;
                """
        results = connectToMySQL(DB).query_db(query, data)
        return (cls(results[0]))
    
    @classmethod
    def add_books_to_fav(cls, data):
        query = """
                INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def not_fav_books(cls, data):
        query = """
                SELECT * FROM books WHERE books.id 
                NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );
                """
        results = connectToMySQL(DB).query_db(query, data)
        not_fav_books = []
        for row in results:
            not_fav_books.append(cls(row))
        
        return not_fav_books
    
    @classmethod
    def get_favorited_by_authors(cls, data):
        query = """
        SELECT * FROM books
        LEFT JOIN favorites ON books.id = favorites.book_id
        LEFT JOIN authors ON favorites.author_id = authors.id
        WHERE books.id = %(id)s
        """
        results = connectToMySQL(DB).query_db(query, data)
        print(results)
        book = cls(results[0])
        for row in results:
            author = {
                'id': row['authors.id'],
                'name': row['name'],
                'created_at': row['authors.created_at'],
                'updated_at': row['authors.updated_at']
            }
            book.favorited_by.append(author_model.Author(author))
        return book