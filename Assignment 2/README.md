# Goat Racing Game

## **Description**


This is an interactive goat racing game where players compete against each other while navigating through obstacles. The game engine manages the racing logic, including player turns, phases, and obstacle interactions. Players take turns making decisions until the race concludes.

## **Features**

- **Multiple Phases**: Progress through various phases, with specific actions allowed in each.
- **Obstacle Management**: Navigate around obstacles placed on the track.
- **Game Logging**: Current state of the game is logged to a file for review.
- **Dynamic Filename Generation**: Automatically creates a timestamped log file for each game session.

## **Usage**
1.  Run the script
2.  Players will take turns, and the game will display the current state.
3.  Input will be required for player actions based on the current phase.
4.  Game logs will be saved in the savegame directory with a timestamp.

## **Game Execution**

The main function initializes the game with:

- **`number_players`**: Total number of players (default is set to 2).
- **`obstacle_positions`**: A list of obstacles defined by their position and type.
- **`filename`**: Automatically generated filename for logging the game state.

```python
if __name__ == '__main__':
    filename = generate_filename()    
    number_players = 2
    obstacle_positions = [(3, 'C'), (6, 'D'), (4, 'F'), (5, 'E'), (4, 'D')]

    main(number_players, obstacle_positions, filename)

## **Log File**

The game state will be saved in a file named `save_{timestamp}.txt` in the `savegame` directory. You can review this file to analyze the game after it ends.

## **Author**

This project was created to provide a fun and engaging way to explore Python programming through game development.
