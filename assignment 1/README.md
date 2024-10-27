## **World Cup Data Processing Program**

###### Description

This program processes data from the FIFA World Cup, providing insights into teams, players, matches, and statistics. It reads data from various text files, including player information, group match results, and yellow card records. The main functionalities of the program include:

**Footballers Data Management**: Reads and organizes footballers' information into a structured dictionary, allowing easy access to player details by country and number.

**Match Analysis**: Reads group match results and calculates the number of goals scored by each team, determining match winners and generating a comprehensive match overview.

**Yellow Card Tracking**: Processes yellow card data for each match, tallying the total yellow cards received by each team throughout the tournament.

**Team Performance Comparison**: Compares teams within groups based on their points, goals, and disciplinary records, determining the top two teams to progress to knockout stages.

**Average Age Calculation**: Computes the average age of footballers for each country and for the overall tournament, offering insights into team demographics.

**Age Histogram Generation**: Creates a histogram to visually represent the distribution of players' ages across participating countries.

**Top Scorer Identification**: Analyzes match data to identify the highest goal scorer of the tournament, displaying their name and corresponding team.

**Yellow Card Analysis**: Identifies and outputs the match with the highest number of yellow cards, detailing the teams and card counts.

###### Files Required
WC22Footballers.txt: Contains data on footballers, including country, position, name, and birthdate.
WC22GroupMatches.txt: Contains results of group stage matches, including teams, scores, and match details.
WC22-YellowCards.txt: Contains records of yellow cards issued during matches.

###### Usage
To run the program, ensure all required data files are in the same directory as the script. Execute the program, and it will process the data, generating several output files and displaying results on the console.

###### Outputs
The program generates the following output files:

groups.txt: Lists the teams in each group.
knockout.txt: Shows the top teams progressing to the knockout stage.
ages.txt: Contains average ages of players by country.
histogram.txt: Displays the age distribution histogram.
scorer.txt: Lists the highest goal scorers in the tournament.
yellow.txt: Details the match with the highest yellow cards.


Author
Samia Rahman
Date: February 6, 2023
