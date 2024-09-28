New! Keyboard shortcuts … Drive keyboard shortcuts have been updated to give you first-letters navigation
'''
Created a program to process the data of the world cup and give the required output
Author: Samia Rahman
Date: 6th Feb, 2023
'''

import codecs

def read_footballers(file):
    '''
    this functions read the data from the footballers txt file and puts everything in a dictionary
    '''

    # Create an empty dictionary to store the data
    footballers = {}
    with codecs.open(file,'r', encoding='utf-8') as f: # Open the file for reading, using UTF-8 encoding
        line = f.readline()
        while line:
            split_line = line.strip().split(';')
            country_number = split_line[0].split()

            # Check the length of the country_number list to determine how to parse the country and number
            if len(country_number) == 3:
                country = country_number[0] + ' ' +country_number[1]
                number = int(country_number[2])
            else: 
                country = country_number[0]
                number = int(country_number[1])
            position, name, birth_date = split_line[1:]

            if country not in footballers:
                footballers[country] = {}
            footballers[country][number] = (position, name, birth_date)
            line = f.readline()  

    return footballers

def read_group_matches(filename):
    '''
    this functions read the data from the group matches txt file and puts everything in a lists of lists
    '''
    group_matches = []
    with open(filename, 'r') as file:
        line = file.readline().strip('\n')

        # continue reading lines until the file is exhausted
        while line:
            values = line.split(';')
            group, team1, team2, goals, date = values
            goals = goals.split(')')
            goals_1 = goals[0][1:].split(',')
            goals_2 = goals[1][1:].split(',')
            # convert goal scorer numbers to integers if possible
            scorers1 = [int(x) if x.isdigit() else x[1:] for x in goals_1]
            scorers2 = [int(x) if x.isdigit() else x[1:] for x in goals_2]
            match = (group, team1, team2, scorers1, scorers2, date) # store match information in a tuple
            group_matches.append(match) # add the match information to the list of matches
            line = file.readline().strip('\n')
    
    return group_matches
        
def read_yellow_cards(filename):
    '''
    Reads the data from the yellow card text file and gives a dictionary which stores the number of yellow cards each team got in each match
    '''
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Initialize an empty dictionary to store the yellow card count for each match
    yellow_card_counts = {}
    for line in lines:
        match, team, *_ = line.strip().split(";")
        team1, team2 = match.split("-")
        
        # If the match is not already in the dictionary, initialize the count for each team as 0
        if match not in yellow_card_counts:
            yellow_card_counts[match] = [0, 0]
        
        # If the team in the line is team1, increase its yellow card count, Else, the team must be team2, so increase its yellow card count
        if team == team1:
            yellow_card_counts[match][0] += 1
        else:
            yellow_card_counts[match][1] += 1
    
    return yellow_card_counts

def get_country_goals(group_matches):
    '''
    This function creates the match as keys and the winner of the match as values
    '''
    a_dict = {}

    for match in group_matches:

        # Create a string to represent the match
        a_string = f'{match[1]}-{match[2]}'

        if a_string not in a_dict:

            a_dict[a_string] = []

            # Calculate the number of goals for each team
            team1 = len(match[3]) if match[3] is not [''] else 0
            team2 = len(match[4]) if match[4] is not [''] else 0

            # compare and Add the winner to the dictionary
            if team1 > team2:
                a_dict[a_string].append(match[1])
            elif team2 > team1:
                a_dict[a_string].append(match[2])
            else:
                a_dict[a_string].append(match[1])
                a_dict[a_string].append(match[2])

        else:

            team1 = len(match[3]) if match[3] is not [''] else 0
            team2 = len(match[4]) if match[4] is not [''] else 0

            if team1 > team2:
                a_dict[a_string].append(match[1])
            elif team2 > team1:
                a_dict[a_string].append(match[2])
            else:
                a_dict[a_string].append(match[1])
                a_dict[a_string].append(match[2])

    return a_dict

def get_country_yellow_card_points(yellow_card_counts):
    '''
    this function creates the countries as keys and the total yellow cards each country got in the world cup as values
    '''
    country_yellow_card = {}

    # Iterate through the dictionary of match-yellow card count
    for match, card_counts in yellow_card_counts.items():
        team1, team2 = match.split("-")

        # If the team doesn't exist in the country-yellow card counts dictionary, add it with count 0
        if team1 not in country_yellow_card:
            country_yellow_card[team1] = 0
        if team2 not in country_yellow_card:
            country_yellow_card[team2] = 0
        
        # Add the yellow card counts for each team to the respective country in the country-yellow card counts dictionary
        country_yellow_card[team1] += card_counts[0]
        country_yellow_card[team2] += card_counts[1]
    
    return country_yellow_card 

def make_groups(group_matches):
    '''
    this function gives a dicitonary of the groups containing the countries
    '''
    groups = {}
    for match in group_matches:
        group, team1, team2, scorers1, scorers2, date = match # unpack the variables from the match tuple
        if group not in groups:
                groups[group] = set() # create a new set for the group if it doesn't already exist in the dictionary
        groups[group].add(team1)
        groups[group].add(team2)

    return groups

def display_groups(groups):
    '''
    this function displays the groups
    '''
    # Print the results to the console and write the results to a file
    for group, teams in sorted(groups.items()): # sorting the groups dictionary by group names
            print("Group " + group )
            for team in sorted(teams): # sorting the teams in each group alphabetically
                print(team)
            print("")

    with open("groups.txt", "w") as new_file:
        for group, teams in sorted(groups.items()):
            new_file.write("Group " + group + "\n")
            for team in sorted(teams):
                new_file.write(team + "\n")
            new_file.write("\n")
            
def get_points(group_matches):
    '''
    this function collects the points based on winning, losing and draws and stores them in a dictionary   
    '''
    points_table = {}
    for match in group_matches:
        group, team1, team2, scorers1, scorers2, date = match
        

        # Calculating the number of goals scored by each team
        for i in scorers1:
            if i == '':
                goals_1 = 0
            else: 
                goals_1 = len(scorers1)
    

        for i in scorers2:
            if i == '':
                goals_2 = 0
            else: 
                goals_2 = len(scorers2)


        # If a team  has scored more goals than the other team, it gets 3 points
        if goals_1 > goals_2:
            if team1 in points_table:
                points_table[team1] += 3
            else:
                points_table[team1] = 3
        elif goals_1 < goals_2:
            if team2 in points_table:
                points_table[team2] += 3
            else:
                points_table[team2] = 3
        
        # If both teams have scored equal number of goals, both teams get 1 point each
        elif goals_1 == goals_2:
            if team1 in points_table:
                points_table[team1] += 1
            else:
                points_table[team1] = 1
            if team2 in points_table:
                points_table[team2] += 1
            else:
                points_table[team2] = 1
    
    match_table_points = {k: v for k, v in points_table.items()}

    return match_table_points

def compare_teams(group_matches, country_yellow_card):
    '''
    this function compares the goals, yellow cards ,red cards between the teams which have similar points and then it gives the top two teams
    
    '''
    points = get_points(group_matches)
    groups = make_groups(group_matches)

    # Create an empty dictionary to store the comparison results
    table = {}

    # For each group, compare the goals, yellow cards, and red cards between the countries
    for group, countries in groups.items():
        # For each country, add the number of points, yellow cards, and red cards to the table
        table[group] = []
        for country in countries:
            yc = country_yellow_card.get(country, 0) # Get the number of yellow cards for the country
            p = points.get(country, 0) # Get the number of points for the country
            table[group].append((country, p, yc)) # Format the table to include the number of red cards for each country
            table[group].sort(key=lambda x: (-x[1], x[2]))

        # Sort the countries by the number of points
        countries =  sorted(countries, key=lambda x: x[1], reverse=True  )

        # Format the table to include the number of red cards for each country
        table = {k: [list(t) for t in v] for k, v in table.items()}


    # For each group, sort the table by the number of points, yellow cards, and red cards
    # and select the top two teams
    for group in table:
        table[group] = [team + [0] if len(team) == 3 else team for team in table[group]]
        table[group].sort(key=lambda x: (x[1], -(x[2] + 4 * x[3])), reverse=True)
        table[group] = table[group][:2]
        

    # Combine the results from each group and sort the teams by their names
    teams = []
    for group in table.values():
        for team in group:
            teams.append(team)

    teams.sort(key=lambda x: x[0])


    # Print the results to the console and write the results to a file
    for team in teams:
        print(f"{team[0]:<12} {team[1]} pts")

    with open("knockout.txt", 'w') as f:
        for team in teams:
            f.write(f'{team[0]:<12} {team[1]} pts \n')

   
    return teams

def average_age(footballers):
    '''
    this function gives me the avergae age of footballers in each country and the overall worldcup
    '''
    average_ages = {}
    for country in footballers:
        ages = []
        for number in footballers[country]:
            # Unpack the values for the current footballer
            position, name, birth_date = footballers[country][number]
            #Split the birth date string to extract the year
            new_birth_date = birth_date.split()
            age = int(new_birth_date[4][:2])
            ages.append(age) # Append the current footballer's age to the list of ages
        
        avg_age = sum(ages) / len(ages)
        average_ages[country] = avg_age

    # Loop through the sorted countries in the average_ages dictionary
    for country in sorted(average_ages.keys(), key=lambda x: x.lower()):
        country = '{:<12}'.format(country)  # Format the country name to have a width of 12 characters
        age = '{:.2f}'.format(average_ages[country.strip()]) # Format the average age to have two decimal places
        print(f'{country} {age} years')
        
    overall_avg = sum(average_ages.values()) / len(average_ages)
    print(f'\nAverage Overall {overall_avg:.2f} years\n')
    
    with open("ages.txt", 'w') as f:
        for country in sorted(average_ages.keys()):
            country = '{:<12}'.format(country)
            age = '{:.2f}'.format(average_ages[country.strip()])
            f.write(f'{country} {age} years\n')
        
        overall_avg = sum(average_ages.values()) / len(average_ages)
        f.write(f'\nAverage Overall {overall_avg:.2f} years\n')

def create_histogram(footballers): 
    '''
    this function displays the histogram of ages 
    '''
    combined_age_of_players = {}

    # Loop through each country in the input dictionary
    for country in footballers:
        ages = []

         # Loop through each footballer in the current country
        for number in footballers[country]:
            position, name, birth_date = footballers[country][number]
            new_birth_date = birth_date.split() # Split the birthdate string to extract the year
            age = int(new_birth_date[4][:2])   # Get the age of the current footballer by extracting the first two characters of the year
            ages.append(age)

        # Loop through each unique age in the list of ages for the current country
        for age in set(ages):
            if age not in combined_age_of_players:  # If the age is not in the combined ages dictionary, add it with a count of 0
                combined_age_of_players[age] = 0
            combined_age_of_players[age] += ages.count(age)

    histogram = {}
    for age, count in combined_age_of_players.items():
        histogram[age] = count

    histogram = sorted(histogram.items()) # Sort the histogram dictionary by age

   
    # Loop through the sorted histogram data and display the histogram information
    for age, count in histogram:
            age_var = str(age) + " years"
            count_var = "(" + str(count).rjust(2) + ")"
            amount = round(count / 5)
            if count >= 5:
                stars = "*" * amount
            else:
                stars = "*"
            print(f"{age_var} {count_var}  {stars}")




    with open("histogram.txt", 'w') as f:
        for age, count in histogram:
                age_var = str(age) + " years"
                count_var = "(" + str(count).rjust(2) + ")"
                amount = round(count / 5)
                if count >= 5:
                    stars = "*" * amount
                else:
                    stars = "*"
                f.write(f"{age_var} {count_var} {stars}\n")


def find_highest_scorer(group_matches, footballers):   
    '''
    this function finds the highest scorers in the entire world cup
    '''
    scorers = {}
    scorer_country = {}

    # Loop through each match in the group matches list
    for match in group_matches:
        # Loop through each team and their goals in the current match
        for team, goals in [(match[1], match[3]), (match[2], match[4])]:
            # Loop through each goal in the goals list
            for goal in goals:
                if goal: # Check if the goal is not empty
                    # If the goal is an integer, it represents player's number
                    # Otherwise, it's the player's name
                    player_number = goal if type(goal) == int else None
                    player_name = goal if type(goal) == str else footballers[team][goal][1]
                    
                    if player_name not in scorers:
                        # Add the player's name and initialize their score to 0
                        scorers[player_name] = 0
                        scorer_country[player_name] = team
                    # Increment the player's score by 1
                    scorers[player_name] += 1


    # Find the highest scorer by getting the player with the maximum score
    highest_scorer = max(scorers, key=scorers.get) if scorers else None
    highest_score = scorers[highest_scorer] if highest_scorer else None
    

    if highest_scorer:
        print("+" + "-" * 15 + ' '+ "+" + ' '+"-" * 16 + ' '+ "+" + ' ' + "-" * 35 + ' '+"+")
        for player, score in scorers.items():
            if score == highest_score:
                player_number = [p[0] for p in footballers[scorer_country[player]].items() if p[1][1] == player][0]
                print("|  {:<13} | {:<16} | {:>2} {:<33}|".format(f"{score} goals", scorer_country[player], player_number, player))

        if highest_scorer:
            print("+" + "-" * 15 + ' '+ "+" + ' '+"-" * 16 + ' '+ "+" + ' ' + "-" * 35 + ' '+"+")
        
        else:
            print("No scorers found.")
    
    with open("scorer.txt", "w") as file:
        if highest_scorer:
            file.write("+" + "-" * 15 + ' '+ "+" + ' '+"-" * 16 + ' '+ "+" + ' ' + "-" * 35 + ' '+ "+\n")
            for player, score in scorers.items():
                if score == highest_score:
                    player_number = [p[0] for p in footballers[scorer_country[player]].items() if p[1][1] == player][0]
                    file.write("|  {:<13} | {:<16} | {:>2} {:<33}|\n".format(f"{score} goals", scorer_country[player], player_number, player))

        if highest_scorer:
            file.write("+" + "-" * 15 + ' '+ "+" + ' '+"-" * 16 + ' '+ "+" + ' ' + "-" * 35 + ' '+ "+\n")
       
        else:
            file.write("No scorers found.")


def highest_yellow_cards(yellow_card):
    '''
    this functions returns the match with the highest yellow cards
    '''
    # find the match with the highest sum of yellow cards
    # retrieve the number of yellow cards for each team
    match = max(yellow_card, key=lambda x: sum(yellow_card[x]))
    team_A, team_B = match.split("-")
    card_count_A, card_count_B = yellow_card[match]

    content = f"{team_A} vs {team_B} \n{team_A}: {card_count_A} YC \n{team_B}: {card_count_B} YC"
    with open("yellow.txt", "w") as file:
        file.write(content)

    print(content)

def main():
    footballers = read_footballers("WC22Footballers.txt")
    group_matches = read_group_matches('WC22GroupMatches.txt')
    yellow_card  = read_yellow_cards('WC22-YellowCards.txt')
     
    make_groups_main = make_groups(group_matches)
    #Question 1: Groups
    display_groups(make_groups_main)
    
    get_country_goals(group_matches)
    country_yellow_card1 = get_country_yellow_card_points(yellow_card)

    #Question 2: Knockout
    compare_teams(group_matches,country_yellow_card1)
    print('\n')

    #Question 3: Average age
    average_age(footballers)
    print('\n')

    #Question 4: Histogram
    create_histogram(footballers)
    print('\n')

    #Question 6: Scorer
    find_highest_scorer(group_matches, footballers)
    print('\n')

    #Question 8: Yellow cards
    highest_yellow_cards(yellow_card)

if __name__ == "__main__":
    main()
