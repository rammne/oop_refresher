# Class Aggregation
# class Player:
#     def __init__(self, name, position, number):
#         # Initialize the name, position, and number properties


# class Team:
#     def __init__(self, name):
#         # Initialize the name property and an empty players list

#     def add_player(self, player):
#         # Add a Player instance to the team's players list

#     def get_player_info(self, number):
#         # Return the player's name, position, and jersey number as a formatted string
#         # or "Player not found" if no player with the given jersey number is found


# # Test your implementation
# player1 = Player("John Doe", "Forward", 10)
# player2 = Player("Jane Smith", "Midfielder", 8)
# player3 = Player("Mark Johnson", "Defender", 4)

# team1 = Team("Dream Team")
# team1.add_player(player1)
# team1.add_player(player2)

# print(team1.get_player_info(10))  # Should output "John Doe (Forward) - 10"
# print(team1.get_player_info(8))   # Should output "Jane Smith (Midfielder) - 8"
# print(team1.get_player_info(4))   # Should output "Player not found"



# ANSWER mine


# class Player:
#     def __init__(self, name, position, number):
#         self.name = name
#         self.position = position
#         self.number = number


# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.players_list = {}

#     def add_player(self, player: Player):
#         self.players_list[player.number] = f'{player.name} ({player.position}) - {player.number}'

#     def get_player_info(self, number):
#         try:
#             return self.players_list[number]
#         except:
#             return 'Player not Found!'


# # Test your implementation
# player1 = Player("John Doe", "Forward", 10)
# player2 = Player("Jane Smith", "Midfielder", 8)
# player3 = Player("Mark Johnson", "Defender", 4)

# team1 = Team("Dream Team")
# team1.add_player(player1)
# team1.add_player(player2)

# print(team1.get_player_info(10))  # Should output "John Doe (Forward) - 10"
# print(team1.get_player_info(8))   # Should output "Jane Smith (Midfielder) - 8"
# print(team1.get_player_info(4))   # Should output "Player not found"


# ANSWER not mine


# # Player class to represent a player in a team
# class Player:
#     def __init__(self, name, position, number):
#         # Initializing the Player with name, position, and number
#         self.name = name  # The name of the player
#         self.position = position  # The position where the player plays
#         self.number = number  # The number of the player in the team
 
# # Team class to represent a team of players
# class Team:
#     def __init__(self, name):
#         # Initializing the Team with name and an empty list of players
#         self.name = name  # The name of the team
#         self.players = []  # The list to store Player instances
 
#     def add_player(self, player):
#         # Method to add a Player instance to the players list
#         self.players.append(player)  # Append the player to the players list
 
#     def get_player_info(self, number):
#         # Method to get player info by number
#         for player in self.players:  # Loop through the players list
#             if player.number == number:  # If the number matches
#                 # Return a formatted string with player information
#                 return f"{player.name} ({player.position}) - {player.number}"
#         # If no player with the specified number is found, return "Player not found"
#         return "Player not found."