from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.friends = []

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s)
                """
        # It returns the id of the created record
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        result = connectToMySQL(DB).query_db(query)
        users = []
        for row in result:
            users.append(cls(row))
        return users
