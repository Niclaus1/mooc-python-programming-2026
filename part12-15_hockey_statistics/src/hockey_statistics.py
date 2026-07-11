# Write your solution here
import json


class Application:
    def __init__(self):
        filename = input("file name: ")
        # filename = "partial.json"
        self.players = self.load_json(filename)
        print(f"read the data of {len(self.players)} players\n")

    def load_json(self, filename: str):
        with open(filename) as my_file:
            data = my_file.read()

        return json.loads(data)

    def search(self):
        print(
            "commands:\n"
            "0 quit\n"
            "1 search for player\n"
            "2 teams\n"
            "3 countries\n"
            "4 players in team\n"
            "5 players from country\n"
            "6 most points\n"
            "7 most goals"
        )
        while True:
            command = input("command:")

            match command:
                case "0":
                    break
                case "1":
                    name = input("name: \n")
                    self.search_player(name)
                    print()

                case "2":
                    self.print_list("team")

                case "3":
                    self.print_list("nationality")

                case "4":
                    team = input("team: ")
                    self.rank_list(team, "team")
                    print()

                case "5":
                    country = input("country: ")
                    self.rank_list(country, "nationality")
                    print()

                case "6":
                    count = int(input("how many:"))
                    players = self.player_rank("points")
                    for i in range(count):
                        self.search_player(players[i]["name"])
                    print()

                case "7":
                    count = int(input("how many:"))
                    players = self.player_rank("goals")
                    for i in range(count):
                        self.search_player(players[i]["name"])
                    print()

    def search_player(self, name: str):
        player = [p for p in self.players if name in p["name"]][0]
        print(
            f"{player['name']:21}{player['team']:4}{player['goals']:3} + {player['assists']:2} = {(player['goals'] + player['assists']):3}"
        )

    def print_list(self, key: str):
        list = set([player[key] for player in self.players])
        for element in sorted(list):
            print(element)
        print()

    def rank_list(self, key: str, reference: str):
        player_list = sorted(
            [p for p in self.players if key in p[reference]],
            key=lambda x: x["assists"] + x["goals"],
            reverse=True,
        )
        for player in player_list:
            self.search_player(player["name"])

    def player_rank(self, key: str):
        if key == "points":
            return sorted(
                [p for p in self.players],
                key=lambda x: (-x["assists"] + -x["goals"], x["goals"]),
            )

        elif key == "goals":
            return sorted(
                [p for p in self.players],
                key=lambda x: (-x["goals"], x["games"]),
            )

        else:
            print()


test = Application()
test.search()
