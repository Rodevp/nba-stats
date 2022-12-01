from requests import get

BASE_URL = "https://data.nba.net"
ALL_OPTIONS_JSON = "/prod/v1/today.json"

response = None

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

    else:
        print("No found results")    


def regular_season() :
    stats = all_links()["leagueTeamStatsLeaders"]
    teams = get(BASE_URL + stats).json()["league"]["standard"]["regularSeason"]["teams"]

    for team in teams :
        name = team["name"]
        nickname = team["nickname"]
        rank = team["ppg"]["rank"]
        average = team["ppg"]["rank"]   

        print("-----------------------------------")    
        print("name - nickname - rank - avg")
        print(name, nickname, rank, average)


def main() :

    print("**NBA INFO**")
    
    while True:

        select_opt = input("Elige una opcion: 1-> Regular Season - 2-> Score Board 3-> Salir. : ")

        if select_opt == "1" :
            regular_season()
            continue
        
        if select_opt == "2" :
            get_score_board()
            continue
        
        if select_opt == "3" :
            print("Thansk, come back later :)")
            break


if __name__ == "__main__" :
    main()