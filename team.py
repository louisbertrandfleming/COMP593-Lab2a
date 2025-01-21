def main():

    # TODO: Step 2 - Create a complex data structure
    team = {
        'name':'Maple Leafs',
        'city':'Toronto',
        'players': [
            'MARNER',
            'TAVARES',
            'MATTHEWS'
        ],
        'games': [
            {
                'opponent': 'Canadiens',
                'goals_for': 8,
                'goals_against': 0
           },
            {
                'opponent': 'Red Wings',
                'goals_for': 3,
                'goals_against': 2
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_game = {
                'opponent': 'Canucks',
                'goals_for': 4,
                'goals_against': 1
            }
    team['games'].append(new_game)
    print_team_name_and_city(team)  # Call the function in Step 4
    
    new_players = ['Domi','Nylander']  # New players for step 5
    add_players(team, new_players)  # Call the step 5 function
    print_players(team)  # Call the step 6 function to print players
    print_opponents(team)  # Call the step 7 function to print opponents

# TODO: Step 4 - Function that prints team name and city
def print_team_name_and_city(team):
    city = team['city']
    lastname = team['name'].split()[1]
    print(f'The {city} {lastname} are the greatest!')
    return

# TODO: Step 5 - Function that adds players to data structure
def add_players(team, players):
    team['players'].extend(players)
    return

# TODO: Step 6 - Function that prints bullet list of players
def print_players(team):
    for player in team['players']:
        print(f' * {player}')
    return

# TODO: Step 7 - Function that prints comma-separated list of opponents
def print_opponents(team):
    opponents = []  # start with an empty list
    for game in team['games']:  # look at games one at a time
        opponents.append(game['opponent'])
    print(opponents)
    return

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return

if __name__ == '__main__':
    main()