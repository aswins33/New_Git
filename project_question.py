import copy   # Import Module

players = []      # Create Empty Lists
jersey_numbers = []
runs_data = []

try:
    n = int(input("Enter number of players: "))     # Taking User Input

    for i in range(n):                  # Loop to Input Player Data
        print(f"\nEnter details for Player {i+1}")

        name = input("Player Name: ")    # Inside the loop:
        jersey = int(input("Jersey Number: "))

        r1 = int(input("Runs in Match 1: "))
        r2 = int(input("Runs in Match 2: "))
        r3 = int(input("Runs in Match 3: "))

        players.append(name)     # Store the Data
        jersey_numbers.append(jersey)
        runs_data.append([r1, r2, r3])

except ValueError:          # Error Handling
    # If user enters: text instead of number for jersey or runs
    print("Invalid input! Please enter numeric values for jersey and runs.")
    exit()

# Create Nested List
# Creates a nested list containing all player information.
player_data = []
for i in range(len(players)):
    player_data.append([players[i], jersey_numbers[i], runs_data[i]])

print("\nPlayer Data (Nested List):")
print(player_data)

# Dictionary using zip()
jersey_dict = dict(zip(jersey_numbers, players))

print("\nJersey Number -> Player Name Dictionary:")
print(jersey_dict)

# String Operations
# Convert Names to Uppercase
print("\nNames in Uppercase:")
for name in players:
    print(name.upper())

print("\nNames longer than 5 characters:")
for name in players:
    if len(name) > 5:                # Names Longer Than 5 Characters
        print(name)

# Count Names Starting with 'R'

count_r = sum(1 for name in players if name.upper().startswith('R'))
print("\nNumber of names starting with 'R':", count_r)

# List Comprehension

# Players with average runs > 50
avg_above_50 = [players[i] for i in range(len(players))
                if sum(runs_data[i])/3 > 50]

print("\nPlayers with average runs greater than 50:")
print(avg_above_50)

# Even jersey numbers
even_jerseys = [j for j in jersey_numbers if j % 2 == 0]
print("\nEven Jersey Numbers:")
print(even_jerseys)

# Convert runs to tuple
first_player_tuple = tuple(runs_data[0])
print("\nFirst Player Runs as Tuple:")
print(first_player_tuple)

# Set of unique run scores
unique_runs = set()
for runs in runs_data:
    unique_runs.update(runs)

print("\nUnique Run Scores:")
print(unique_runs)

# Shallow Copy
# Creates a copy of the outer list only.
shallow_copy = player_data.copy()

# Deep Copy
# Creates completely independent copy.
deep_copy = copy.deepcopy(player_data)

print("\nShallow Copy of Player Data:")
print(shallow_copy)
                                                 # Displays both copied lists.
print("\nDeep Copy of Player Data:")
print(deep_copy)