class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(
        "first name:", self.first_name + "\n" +
        "last name:", self.last_name + "\n" +
        "email:", self.email + "\n" +
        "age:", str(self.age) + "\n" +
        "rewards member:", str(self.is_rewards_member) + "\n" +
        "gold card points:", self.gold_card_points
        )

    def enroll(self):
        if (self.is_rewards_member == True):
            # self.is_rewards_member = False
            return f"{self.first_name} already a member."
        else:
            self.is_rewards_member = True
            print("Enrolled Successfully!")
        self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Not enough points")


user1 = User("Mouadh", "Jenouiz", "mouadhjenouiz@gmail.com", 35)
user1.display_info()

user2 = User("John", "Doe", "johndoe@gmail.com", 25)
user3 = User("Jane", "Doe", "janedoe@gmail.com", 22)

user1.spend_points(50)

user2.enroll()
user2.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()

user3.spend(40)
