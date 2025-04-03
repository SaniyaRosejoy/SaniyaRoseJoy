games = [
    {"name": "PUBG", "editor": "Krafton", "year": 2017}
]

new_game_name = input("Enter the name of the game:\n")
new_game_editor = input("Enter the editor of the game:\n")
new_game_year = input("Enter the release year of the game:\n")

new_game = {
    "name": new_game_name,
    "editor": new_game_editor,
    "year": new_game_year
}

games.append(new_game)

for game in games:
    print(f"Name: {game["name"]} - Editor : {game["editor"]} - Year: {game["year"]}")