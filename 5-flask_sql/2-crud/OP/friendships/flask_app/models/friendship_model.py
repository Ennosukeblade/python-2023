from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash


class Friendship:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO friendships (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s)
                """
        # It returns the id of the created record
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def friendship_exists(cls, data):
        query = """
        SELECT * FROM friendships WHERE 
        user_id = %(user_id)s AND friend_id = %(friend_id)s
        OR user_id = %(friend_id)s AND friend_id = %(user_id)s
        """
        # It returns the id of the created record
        return connectToMySQL(DB).query_db(query, data)

    @staticmethod
    def validate_relation(data):
        is_valid = True
        if data['user_id'] == data['friend_id']:
            is_valid = False
            # flash("Invalid relationship, choose a different user!", "relationship")
            flash("Invalid relationship, choose a different user!")
        if len(Friendship.friendship_exists(data)) != 0:
            is_valid = False
            # flash("Invalid relationship, choose a different user!", "relationship")
            flash("Already friends, choose a another user!")
        return is_valid
