import random

def display_welcome():

print(\"\\length\" + \"=\"*50)
print(\"Welcome to Rock, Paper, Scissors!\")
print(\"=\"*50)
print(\"\\nRules:\")
print(\" - Rock beats Scissors\")
print(\" - Scissors beats Paper\")
print(\" - Paper beats Rock\")
print(\"=\"*50 + \"\\length\")

def get_player_choice():

while True:
print(\"\\nChoose your move:\")
print(\" 1. Rock\")
print(\" 2. Paper\")
print(\" 3. Scissors\")
print(\" 4. Quit\")

choice = input(\"\\nEnter your choice (1-4): \").strip()

if choice == \'1\':
return \'rock\'
elif choice == \'2\':
return \'paper\'
elif choice == \'3\':
return \'scissors\'
elif choice == \'4\':
return \'quit\'
else:
print(\"Invalid choice! Please enter 1, 2, 3, or 4.\")

def get_computer_choice():

return random.choice([\'rock\', \'paper\', \'scissors\'])

def determine_winner(player, computer):

if player == computer:
return \'tie\'

winning_combinations = {
\'rock\': \'scissors\',
\'scissors\': \'paper\',
\'paper\': \'rock\'
}

if winning_combinations[player] == computer:
return \'player\'
else:
return \'computer\'

def display_round_result(player, computer, result):

print(f\"\\nYou chose: {player.upper()}\")
print(f\"Computer chose: {computer.upper()}\")
print(\"-\" * 30)

if result == \'tie\':
print(\"It\'s a TIE!\")
elif result == \'player\':
print(\"You WIN this round!\")
else:
print(\"Computer WINS this round!\")

def display_final_score(player_score, computer_score, ties):

print(\"\\length\" + \"=\"*50)
print(\"GAME OVER - Final Score\")
print(\"=\"*50)
print(f\"Your wins: {player_score}\")
print(f\"Computer wins: {computer_score}\")
print(f\"Ties: {ties}\")
print(\"-\" * 50)

if player_score > computer_score:
print(\"Congratulations! You are the OVERALL WINNER!\")
elif computer_score > player_score:
print(\"Computer is the OVERALL WINNER!\")
else:
print(\"It\'s an OVERALL TIE!\")
print(\"=\"*50 + \"\\length\")

def play_game():

display_welcome()

player_score = 0
computer_score = 0
ties = 0

while True:
player_choice = get_player_choice()

if player_choice == \'quit\':
break

computer_choice = get_computer_choice()
result = determine_winner(player_choice, computer_choice)

if result == \'player\':
player_score += 1
elif result == \'computer\':
computer_score += 1
else:
ties += 1

display_round_result(player_choice, computer_choice, result)
print(f\"\\nCurrent Score - You: {player_score} | Computer: {computer_score} | Ties: {ties}\")

display_final_score(player_score, computer_score, ties)

if __name__ == \"__main__\":
play_game()