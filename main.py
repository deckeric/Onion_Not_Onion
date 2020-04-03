import csv
import random

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


titles = []
onion = []
players = []


with open('OnionOrNot.csv', encoding="utf8", errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        titles.append(row[0])
        onion.append(row[1])
        line_count += 1
    # print(f'Processed {line_count} lines.')
    game = True
    while(game):
        num_of_players = int(input("Hi welcome to Onion or Not the Onion. How many players are there? "))
        for p in range(1, num_of_players+1):
            name = input(f"Name of player {p} ")
            players.append(Player(name, 0))
        win = int(input("How many points do you want to play to? "))
        print("-"*45)
        # for obj in players:
        #     print(f'Name: {obj.name} with a Score of: {obj.score}')
        playing = True
        start = random.randint(0, num_of_players - 1)
        while(playing):
            if start > num_of_players-1:
                start = 0
                print("-" * 45)
                for obj in players:
                    print(f'Name: {obj.name} with a Score of: {obj.score}')
                print("-" * 45)
            print(f"\nAlright {players[start].name} its your turn!")
            random_num = random.randint(1, line_count)
            print(f"\nTITLE:\n{titles[random_num]}")
            answer = input("\nIs it onion or not the onion? Type O for Onion. Type N for Not the Onion. ")
            answer = answer.upper()
            print("-" * 45)
            while(answer != 'O' and answer != 'N'):
                print("That is not a valid input.")
                answer = input("\nIs it onion or not the onion? Type O for Onion. Type N for Not the Onion. ")
                answer = answer.upper()
            if answer == 'O':
                guess = 1
            elif answer == 'N':
                guess = 0
            if guess == int(onion[random_num]):
                print("Correct!")
                print("-" * 45)
                players[start].score +=1
            else:
                print("Sorry, not right!")
                print("-" * 45)
            start +=1
            for obj in players:
                if obj.score == win:
                    print(f"{obj.name} wins!")
                    playing = False
        new_game = input("Would you like to play again? Y or N ")
        new_game = new_game.upper()
        while (new_game != 'Y' and new_game != 'N'):
            print("That is not a valid input.")
            new_game = input("Would you like to play again? Y or N ")
            new_game = new_game.upper()
        if new_game == 'N':
            game = False