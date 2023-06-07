from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models.book_model import Book


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_books = []

    @classmethod
    def get_all_authors(cls):
        query = """
                SELECT * from authors;
                """
        results = connectToMySQL(DB).query_db(query)
        authors = []
        for row in results:
            authors.append(cls(row))
        return (authors)

    @classmethod
    def add_author(cls, data):
        query = """
                INSERT INTO authors (name) VALUES (%(name)s)
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_author_by_id(cls, data):
        query = """
                SELECT * from authors WHERE id = %(id)s;
                """
        results = connectToMySQL(DB).query_db(query, data)
        return (cls(results[0]))
    
    @classmethod
    def get_fav_books(cls, data):
        query = """
        SELECT * FROM authors
        LEFT JOIN favorites ON authors.id = favorites.author_id
        LEFT JOIN books ON favorites.book_id = books.id
        WHERE authors.id = %(id)s
        """
        results = connectToMySQL(DB).query_db(query, data)
        print(results)
        author = cls(results[0])
        for row in results:
            book = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at']
            }
            author.fav_books.append(Book(book))
        return author
    
    @classmethod
    def not_favorited_by_authors(cls, data):
        query = """
                SELECT * FROM authors WHERE authors.id 
                NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );
                """
        results = connectToMySQL(DB).query_db(query, data)
        not_fav_by_authors = []
        for row in results:
            not_fav_by_authors.append(cls(row))
        
        return not_fav_by_authors
    
    @classmethod
    def add_author_to_fav(cls, data):
        query = """
                INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);
                """
        return connectToMySQL(DB).query_db(query, data)
