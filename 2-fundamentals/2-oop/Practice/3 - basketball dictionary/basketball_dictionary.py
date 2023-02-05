class Player:
    players_list = []

    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]
        Player.players_list.append(self)

    @classmethod
    def all_players(cls):
        players = []
        for player in cls.players_list:
            print (player.name)
        #return players    

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}
# player1 = Player({"name": "mouadh", "age": 35,"position": "Power Forward", "team": "Tunisia"})
# print(player1.name)

kevin = Player(kevin)
jason = Player(jason)
kyrie = Player(kyrie)

print(kevin.name, jason.name, kyrie.name)
Player.all_players()
