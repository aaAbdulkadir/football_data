# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd 

def scrape_stat(url, stat_col):
    # get content
    website = requests.get(url).content
    # use beautifulsoup to parse data
    soup = BeautifulSoup(website, 'lxml')

    # card for top players
    card = soup.find(class_='card mb10')

    # list of players name and stats
    name = []
    stat = []

    # name and stat
    top_name = card.find(class_='card-subtitle mb-2 player_name').text
    name.append(top_name)
    top_stat = card.find(class_='player-value').text
    stat.append(top_stat)

    # rest of players in top scorer card
    rest_name = card.find_all(class_='c_name')
    for player in rest_name:
        name.append(player.text.strip().split('|')[0])

    rest_stat = card.find_all(class_='c_value')
    for player in rest_stat:
        stat.append(player.text)

    df = pd.DataFrame({'Name': name, f'{stat_col}': stat})
    df.to_csv(f'data/{stat_col}_table.csv')

final_stat_links = {
    'top_goals': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Goals',
    'top_assists': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Goal%20Assists',
    'top_expected_goals': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/xG',
    'top_expected_assists': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/xA',
    'top_shots_on_target': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Shots%20On%20Target%20(%20inc%20goals%20)',
    'top_shots': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Shots%20For',
    'top_chances_created': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Chance%20Created',
    'top_successful_dribbles': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Successful%20Dribbles',
    'top_tackles_won': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Tackles%20Won', 
    'top_red_cards': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Total%20Red%20Cards',
    'top_fouls_won': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Total%20Fouls%20Won',
    'top_tackles_won': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Tackles%20Won',
    'top_interceptions': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Interceptions',
    'top_clearances': 'https://analytics.soccerment.com/en/league/premier_league/players/stat/Total%20Clearances' 
}

for key, value in final_stat_links.items():
    scrape_stat(value, key)