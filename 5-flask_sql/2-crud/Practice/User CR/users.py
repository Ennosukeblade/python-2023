from mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
 
    # 1) we use class methods to query our database
    @classmethod
    def get_all_users(cls):

        query = "SELECT * FROM users;"
        result = connectToMySQL('users_schema').query_db(query)
        # print(result)

        all_users = []
        # Iterate over the db results and create instances of users with cls.
        for user in result:
            all_users.append(cls(user))
        
        #print(all_users)
        return all_users

    @classmethod
    def add_user(cls, data):

        query = """
                INSERT INTO users (first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s );
                """
        result = connectToMySQL('users_schema').query_db(query, data)
        print(result)
        return result