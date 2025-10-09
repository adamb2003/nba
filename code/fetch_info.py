import requests
import pandas as pd

url = "https://nbafantasy.nba.com//api/bootstrap-static/"
data = requests.get(url).json()

players = pd.DataFrame(data["elements"])
players_clean = players.assign(
    name = players["first_name"] + " " + players["second_name"]
)[["id", "name", "now_cost", "team", "element_type", "status"]]

players_clean.to_csv("player_info.csv", index=False)
