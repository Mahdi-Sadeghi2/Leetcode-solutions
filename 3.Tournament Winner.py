# Constant to represent when the home team won (makes code more readable than using 1 directly)
HOME_TEAM_WON = 1

# Function to determine the tournament winner
# Time Complexity: O(n) where n is the number of competitions
# Space Complexity: O(k) where k is the number of teams (stored in the scores dictionary)


def tournament_winner(competitions, results):
    # Initialize tracking for the current best team (starts as empty string)
    current_best_team = ""

    # Dictionary to keep track of each team's total points (starts with empty team having 0 points)
    scores = {current_best_team: 0}

    # Iterate through each competition and its corresponding result
    for index, competition in enumerate(competitions):
        result = results[index]
        home_team, away_team = competition

        # Determine the winning team based on the result
        winning_team = home_team if result == HOME_TEAM_WON else away_team

        # Update the scores for the winning team (3 points per win)
        update_scores(winning_team, 3, scores)

        # Update current best team if this team's score exceeds the current best
        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team

    # After processing all competitions, return the team with the highest score
    return current_best_team

# Helper function to update a team's score in the scores dictionary


def update_scores(team, points, scores):
    # Initialize the team's score to 0 if they're not already in the dictionary
    if team not in scores:
        scores[team] = 0

    # Add the points to the team's current score
    scores[team] += points
