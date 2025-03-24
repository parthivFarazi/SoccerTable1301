import streamlit as st 
import os
import pandas as pd
import requests


# Create navigation sidebar
st.sidebar.title("League Table")
league_choice = st.sidebar.radio("Select a league", ["English Premier League", "Spanish La Liga", "Italian Serie A", "French League 1"])
season_year = st.sidebar.number_input("Year", min_value=2012, max_value=2023, value=2023)
year=season_year-1
leagueforapi = ""
leaguelogo=""
if league_choice == "English Premier League":
    leagueforapi = "eng.1"
    leaguelogo="https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Premier_League_Logo.svg/640px-Premier_League_Logo.svg.png"
elif league_choice == "Spanish La Liga":
    leagueforapi = "esp.1"
    leaguelogo="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/LaLiga_logo_2023.svg/2048px-LaLiga_logo_2023.svg.png"
elif league_choice == "Italian Serie A":
    leagueforapi = "ita.1"
    leaguelogo="https://1000logos.net/wp-content/uploads/2019/01/Italian-Serie-A-Logo.png"
elif league_choice == "French League 1":
    leagueforapi = "fra.1"
    leaguelogo="https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Ligue_1_Uber_Eats_logo.svg/1200px-Ligue_1_Uber_Eats_logo.svg.png"
url=("https://api-football-standings.azharimm.dev/leagues/{}/standings?season={}&sort=asc").format(leagueforapi,year)
r=requests.get(url)
data=r.json()



def leagueTable (league_choice):
    st.image(leaguelogo, width=300)
    st.title(f"{league_choice} Table {season_year-1}-{season_year}")
    league_data = {
    "rank":[],
    #"logo":[], 
    "name":[], 
    "gamesPlayed":[],
    "points":[],
    "wins":[],
    "draws":[],
    "losses":[],
    "gFor":[],
    "gAgainst":[],
    "gDif":[],
    }

    theData=(data['data']['standings'])
    for num in range(len(theData)):  
        league_data["rank"]+= [(num+1)]
        league_data["name"]+= [data['data']['standings'][num]['team']['name']]
        league_data["gamesPlayed"]+= [data['data']['standings'][num]['stats'][0]['value']]
        league_data["points"]+= [data['data']['standings'][num]['stats'][3]['value']]
        league_data["wins"]+= [data['data']['standings'][num]['stats'][7]['value']]
        league_data["draws"]+= [data['data']['standings'][num]['stats'][6]['value']]
        league_data["losses"]+= [data['data']['standings'][num]['stats'][1]['value']]
        league_data["gFor"]+= [data['data']['standings'][num]['stats'][5]['value']]
        league_data["gAgainst"]+= [data['data']['standings'][num]['stats'][4]['value']]
        league_data["gDif"]+= [data['data']['standings'][num]['stats'][2]['value']]
    
    the_table = pd.DataFrame(league_data)
    st.dataframe(the_table, column_config={
        "rank": "Rank",
        "name": "Team Name",
        "gamesPlayed": "Games Played",
        "points":"Points",
        "wins":"Wins",
        "draws":"Draws",
        "losses":"Losses",
        "gFor":"Goals For",
        "gAgainst":"Goals Against",
        "gDif":"Goal Difference"},

        hide_index=True,
        )
    

if league_choice == "English Premier League":
    leagueTable("English Premier League")
elif league_choice == "Spanish La Liga":
    leagueTable("Spanish La Liga")
elif league_choice == "Italian Serie A":
    leagueTable("Italian Serie A")
elif league_choice == "French League 1":
    leagueTable("French League 1")












    


