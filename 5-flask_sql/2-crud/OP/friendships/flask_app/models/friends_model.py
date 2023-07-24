from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB


class Friends:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.friend_first_name = data['friend_first_name']
        self.friend_last_name = data['friend_last_name']

    @classmethod
    def get_friendships(cls):
        query = """
                SELECT user1.first_name, user1.last_name, user2.first_name, user2.last_name
                FROM users AS user1
                JOIN friendships ON user1.id = friendships.user_id
                JOIN users AS user2 ON user2.id = friendships.friend_id;
                """
        result = connectToMySQL(DB).query_db(query)
        print(result)
        friends = []
        for row in result:
            friend = {
                **row,
                'friend_first_name': row['user2.first_name'],
                'friend_last_name': row['user2.last_name']
            }
            friends.append(cls(friend))
        print(friends)
        return friends
