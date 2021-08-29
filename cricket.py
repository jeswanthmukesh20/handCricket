import random


class Validator:
    def input_validator(self, greater=None, smaller=None, team=None):
        i = 1
        if team is None:
            while i <= 3:
                inp = input(f"[*]Enter input between {smaller}-{greater}: ")
                if inp.isdigit():
                    inp = int(inp)
                    if smaller <= inp <= greater:
                        return inp
                    elif smaller > inp:
                        print(f'\nYour value should be greater than {smaller}')
                    else:
                        print(f'\nYour value should be lesser than {greater}')
                else:
                    print('\nEnter valid input!')
                i += 1
                if i > 3:
                    print('\nToo many tries!')
        else:
            i = 1
            while i <= 3:
                print("\nChoose your team name\n")
                inp = input('CSK, MI, DC, KKR, RCB, SRH, KXIP, RR:\t').upper()
                if inp.isalpha():
                    if inp in team:
                        return inp
                    else:
                        print('\nEnter valid team name correctly!')
                else:
                    print('\nEnter valid input!')
                i += 1
                if i > 3:
                    print('\nToo many tries!')
        if i > 3:
            raise ValueError


class Player(Validator):
    def __init__(self, who, players=None, Team_name=None):
        if who == 'Human':
            self.score = 0
            print('\nHow many players do you want?\t')
            self.players = self.input_validator(smaller=3, greater=10)
            print("\nHow many overs\t")
            self.overs = self.input_validator(smaller=1, greater=20)
            li = 'CSK, MI, DC, KKR, RCB, SRH, KXIP, RR'.split(', ')
            self.Team = self.input_validator(team=li)

        else:
            self.players = players
            self.Team = Team_name
            self.score = 0


class Game(Validator):

    def __init__(self, player1, player2):
        self.winner = None
        self.tos = None
        self.initial_human = player1.players
        self.initial_bot = player2.players
        self.toss()
        self.get_toss()

    def toss(self):
        i = 0

        while i <= 3:
            print('\nodd or even?')
            tos = input('[O/E]').lower()
            if not tos.isalpha():
                print('\nThe choice is only string!')
            elif tos in ['odd', 'od', 'o', 'even', 'eve', 'e']:
                print('\nFine!')
                break
            else:
                print('\nEnter valid input!')
            i += 1
        if i > 3:
            raise ValueError

        self.tos = tos

    def get_toss(self):
        print('\nEnter number between 1 to 6')
        choice = self.input_validator(smaller=1, greater=6)

        bot = random.randint(1, 6)
        ans = (choice + bot) % 2
        if (
            self.toss in ['odd', 'od', 'o']
            and ans != 0
            or self.toss not in ['odd', 'od', 'o']
            and ans == 0
        ):
            self.winner = 'Human'
            print(f'\n{player1.Team} won the toss!')
        else:
            self.winner = 'Bot'
            print(f'\n{player2.Team} won the toss!')
        if self.winner == 'Human':
            while True:
                bat_or = input('\nBatting or Bowling?\t').lower()
                if bat_or.isalpha():
                    if bat_or in ['batting', 'bat', 'ba']:
                        self.first = player1.Team
                        print(f'{player1.Team} won the toss and choose to bat first!')
                    else:
                        self.first = player2.Team
                        print(f'{player1.Team} won the toss and choose to bowl!')
                    break
        else:
            bot_choice = random.choice(['bat', 'bowl'])
            if bot_choice == 'bat':
                self.first = player2.Team
                print(f'{player2.Team} won the toss and choose to bat first!')
            else:
                self.first = player1.Team
                print(f'{player2.Team} won the toss and choose to bowl!')

    def score_card(self, player, target):
        if target and player.Team == player1.Team:
            if player.players == self.initial_human:
                print(f"\n{player.Team}: {player.score} Overs: {self.over[0]}.{self.over[1]}")
            else:
                print(
                    f'\n{player.Team}: {player.score}/{self.initial_human - player1.players} Overs: {self.over[0]}.{self.over[1]}\t Target: {player2.score + 1}')
        elif not target and player.Team == player1.Team:
            if player.players == self.initial_human:
                print(f"\n{player.Team}: {player.score} Overs: {self.over[0]}.{self.over[1]}")
            else:
                print(
                    f'\n{player.Team}: {player.score}/{self.initial_human - player1.players} Overs: {self.over[0]}.{self.over[1]}')
        elif target and player.Team == player2.Team:
            if player.players == self.initial_bot:
                print(f"\n{player.Team}: {player.score} Overs: {self.over[0]}.{self.over[1]}")
            else:      
                print(
                    f'\n{player.Team}: {player.score}/{self.initial_bot - player2.players} Overs: {self.over[0]}.{self.over[1]}\t Target: {player1.score + 1}')
        elif not target and player.Team == player2.Team:
            if player.players == self.initial_bot:
                print(f"\n{player.Team}: {player.score} Overs: {self.over[0]}.{self.over[1]}")
            else:
                print(
                    f'\n{player.Team}: {player.score}/{self.initial_bot - player2.players} Overs: {self.over[0]}.{self.over[1]}')

    def batting(self, player, target):
        if not target and player.Team == player1.Team:
            self.over = [0, 0]
            while (player1.players > 1) and (self.over[0] != player1.overs):
                for _ in range(6):
                    score = self.input_validator(greater=6, smaller=1)
                    bot = random.randint(1, 6)
                    if score != bot:
                        player.score += score
                    else:
                        player.players -= 1
                        print("\n That's a wicket!")
                    if self.over[1] < 5:
                        self.over[1] += 1
                    else:
                        self.over[0] += 1
                        self.over[1] = 0
                    self.score_card(player=player1, target=False)

        elif target and player.Team == player1.Team:
            self.over = [0, 0]
            while (player.overs != self.over[0]) and (player1.players > 1):
                if player.score >= player2.score:
                    break
                for _ in range(6):
                    score = self.input_validator(greater=6, smaller=1)
                    bot = random.randint(1, 6)
                    if score != bot:
                        player1.score += score
                    else:
                        player1.players -= 1
                        print("\nThat's a wicket!")
                    if self.over[1] < 5:
                        self.over[1] += 1
                    else:
                        self.over[0] += 1
                        self.over[1] = 0
                    self.score_card(player=player1, target=True)
                    if player.score == player2.score:
                        print("\nMatch Draw!")
                    elif player.score > player2.score:
                        break

        elif not target and player.Team == player2.Team:
            self.over = [0, 0]
            while (self.over[0] != player2.overs) and player2.players > 1:
                for _ in range(6):
                    score = random.randint(1, 6)
                    bot = self.input_validator(greater=6, smaller=1)
                    if score != bot:
                        player2.score += score
                    else:
                        player2.players -= 1
                        print("\nThat's a wicket!")
                    if self.over[1] < 5:
                        self.over[1] += 1
                    else:
                        self.over[0] += 1
                        self.over[1] = 0
                    self.score_card(player=player2, target=False)

        elif target and player.Team == player2.Team:
            self.over = [0, 0]
            while (self.over[0] != player2.overs) and player2.players > 1:
                if player.score > player1.score:
                    break
                for _ in range(6):
                    score = random.randint(1, 6)
                    bot = self.input_validator(greater=6, smaller=1)
                    if score != bot:
                        player2.score += score
                    else:
                        player2.players -= 1
                        print("\nThat's a wicket!")
                    self.score_card(player=player2, target=True)
                    if player.score == player1.score:
                        print("\nMatch Draw!")
                    elif player.score > player1.score:
                        break
                    if self.over[1] < 5:
                        self.over[1] += 1
                    else:
                        self.over[0] += 1
                        self.over[1] = 0

    def game(self):
        if self.first == player1.Team:
            self.batting(player=player1, target=False)
            print("2nd Innings")
            self.batting(player=player2, target=True)
        else:
            self.batting(player=player2, target=False)
            print("2nd Innings")
            self.batting(player=player1, target=True)

        if player2.score > player1.score:
            print(f"{player2.Team} won! the match!")
            print("\nYou lose!")
        elif player2.score < player1.score:
            print(f"\n{player1.Team} won the match!")
        else:
            print("\nMatch draw!")


if __name__ == "__main__":
    try:
        player1 = Player(who="Human")
        lis = 'CSK, MI, DC, KKR, RCB, SRH, KXIP, RR'.split(', ')
        lis.remove(player1.Team)
        player2 = Player(who="Bot", players=player1.players, Team_name=random.choice(lis))
        player2.overs = player1.overs
        g = Game(player1=player1, player2=player2)
        g.game()

    except Exception as e:
        print(f'{e}Sorry!\n')
        print("Come again!")
