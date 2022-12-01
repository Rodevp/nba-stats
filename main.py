from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_OPTIONS_JSON = "/prod/v1/today.json"

response = None
printer = PrettyPrinter()


def all_links() :

    try: 
        response = get(BASE_URL + ALL_OPTIONS_JSON).json()
    except TypeError as e :
        print("Error get requests")
    
    return response["links"]


def get_score_board() : 

    score_board_link = all_links()["currentScoreboard"]
    data = None

    try:
        data = get(BASE_URL + score_board_link)
    except TypeError as e :
        print("Error requests")


    if data.status_code == 200 :
        
        data = data.json()
        
        for game in data :

            home_team = game["hTema"]
            away_team = game["aTeam"]
            clock_match = game["clock"] 
            period = game["period"]   

            print("----------------------------------------------")
            print(f"{home_team['triCode']} vs {away_team['triCode']}")
            print(f"{home_team['score']} - {away_team['score']}")
            print(f"{clock_match} - {period['current']}")


get_score_board()


