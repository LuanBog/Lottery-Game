#self.player = [{'player': Player, 'numbers': [int, int], 'bet': int}]

import random
import time
from operator import itemgetter

NAME = input("\nEnter your name: ")
CREDIT_PIN = int(input("Credit Pin: "))
MONEY = 30

MIN = 1
MAX = 10

contestant_names = ["Liam","Noah","William","James","Oliver","Benjamin","Elijah","Lucas","Mason","Logan","Alexander","Ethan","Jacob","Michael","Daniel","Henry","Jackson","Sebastian","Aiden","Matthew","Samuel","David","Joseph","Carter","Owen","Wyatt","John","Jack","Luke","Jayden","Dylan","Grayson","Levi","Isaac","Gabriel","Julian","Mateo","Anthony","Jaxon","Lincoln","Joshua","Christopher","Andrew","Theodore","Caleb","Ryan","Asher","Nathan","Thomas","Leo","Isaiah","Charles","Josiah","Hudson","Christian","Hunter","Connor","Eli","Ezra","Aaron","Landon","Adrian","Jonathan","Nolan","Jeremiah","Easton","Elias","Colton","Cameron","Carson","Robert","Angel","Maverick","Nicholas","Dominic","Emma","Olivia","Ava","Isabella","Sophia","Charlotte","Mia","Amelia","Harper","Evelyn","Abigail","Emily","Elizabeth","Mila","Ella","Avery","Sofia","Camila","Aria","Scarlett","Victoria","Madison","Luna","Grace","Chloe","Penelope","Layla","Riley","Zoey","Nora","Lily","Eleanor","Hannah","Lillian","Addison","Aubrey","Ellie","Stella","Natalie","Zoe","Leah","Hazel","Violet","Aurora","Savannah","Audrey","Brooklyn","Bella","Claire","Skylar","Lucy","Paisley","Everly","Anna","Caroline","Nova","Genesis","Emilia","Kennedy","Samantha","Maya","Willow","Kinsley","Naomi","Aaliyah","Elena","Sarah","Ariana","Allison","Gabriella","Alice","Madelyn","Cora","Ruby","Eva","Serenity","Autumn","Adeline","Hailey","Gianna","Valentina","Isla","Eliana","Quinn","Nevaeh","Ivy","Sadie","Piper","Lydia","Alexa","Josephine","Emery","Julia","Delilah","Arianna","Vivian","Kaylee","Sophie","Brielle","Madeline","Peyton","Rylee","Clara","Hadley","Melanie","Mackenzie","Reagan","Adalynn","Liliana","Aubree","Jade","Katherine","Isabelle","Natalia","Raelynn","Maria","Athena","Ximena","Arya","Leilani","Taylor","Faith","Rose","Kylie","Alexandra","Mary","Margaret","Lyla","Ashley","Amaya","Eliza","Brianna","Bailey","Andrea","Khloe","Jasmine","Melody","Iris","Isabel","Norah","Annabelle","Valeria","Emerson","Adalyn","Ryleigh","Eden","Emersyn","Anastasia","Kayla","Alyssa","Juliana","Charlie","Esther","Ariel","Cecilia","Valerie","Alina","Molly","Reese","Aliyah","Lilly","Parker","Finley","Morgan","Sydney","Jordyn","Eloise","Trinity","Daisy","Kimberly","Lauren","Genevieve","Sara","Arabella","Harmony","Elise","Remi","Teagan","Alexis","London","Sloane","Laila","Lucia","Diana","Juliette","Sienna","Elliana","Londyn","Ayla","Callie","Gracie","Josie","Amara","Jocelyn","Daniela","Everleigh","Mya","Rachel","Summer","Alana","Brooke","Alaina","Mckenzie","Catherine","Amy","Presley","Journee","Rosalie","Ember","Brynlee","Rowan","Joanna","Paige","Rebecca","Ana","Sawyer","Mariah","Nicole","Brooklynn","Payton","Marley","Fiona","Georgia","Lila","Harley","Adelyn","Alivia","Noelle","Gemma","Vanessa","Journey","Makayla","Angelina","Adaline","Catalina","Alayna","Julianna","Leila","Lola","Adriana","June","Juliet","Jayla","River","Tessa","Lia","Dakota","Delaney","Selena"]

print()

def filter_pin(pin):
    pin = str(pin)
    filtered = ""

    filtered = pin[0]
    filtered = filtered + "*" * (len(pin)-2)
    filtered = filtered + pin[-1]

    return filtered

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def increase(self, money):
        self.money += money

    def decrease(self, money):
        self.money -= money

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

class Game:
    def __init__(self, min_bet=10, first=-1, second=-1, third=-1, min=MIN, max=MAX):
        self.players = []
        self.pot = 0
        self.first = first
        self.second = second
        self.third = third
        self.min = min
        self.max = max
        self.min_bet = min_bet

        if self.first < 0 and self.second < 0 and self.third < 0:
            self.first, self.second, self.third = self.get_random_numbers()

    def add_player(self, player, numbers, bet):
        input_ = {"player": player, "numbers": numbers, "bet": bet, "name": player.get_name()} #Name is not used in those whole code (for the sake of fucking sorting and organization)

        self.players.append(input_)
        self.pot += bet

        self.players.sort(key=itemgetter("name"))

    def get_random_numbers(self):
        first = random.randrange(self.min, self.max)
        second = random.randrange(self.min, self.max)
        third = random.randrange(self.min, self.max)

        return [first, second, third]

    def get_winners(self):
        winners = []

        for player in self.players:
            player_first, player_second, player_third = player["numbers"]

            if player_first == self.first and player_second == self.second and player_third == self.third:
                winners.append(player)

        return winners

    def get_min_bet(self):
        return self.min_bet

    def run(self):
        winners = self.get_winners()

        print("Processing winners with {} contestants, and pot of ₱{}...".format(len(self.players), self.pot))

        time.sleep(3)

        print("The winner is...")

        time.sleep(3)

        print("")

        if winners:
            print("\"{}\"! with the number of {}, {} and {}. He or she or they betted ₱{}. The pot of ₱{} is now his or hers or theirs!".format(', '.join([player["player"].get_name() for player in winners]), self.first, self.second, self.third, ', ₱'.join([str(player["bet"]) for player in winners]), self.pot))

            for player in winners:
                player["player"].increase(self.pot)
            
            self.pot = 0
        else:
            print("Nobody wins! The correct numbers were {}, {} and {}. Thanks for playing! Try again if there is another if you want!".format(self.first, self.second, self.third))

        time.sleep(5)

        print("")
        print("-"*65)
        print("{:<12} {:>12} {:>19} {:>18}".format("NAME", "BET", "NUMBERS", "WON"))
        print("-"*65)
        for player in self.players:
            if player in winners:
                print("{:<12} {:>12} {:>18} {:>18}".format(player["player"].get_name(), "₱" + str(player["bet"]), str(player["numbers"][0]) +  " " + str(player["numbers"][1]) + " " + str(player["numbers"][2]), "/"))
            else:
                print("{:<12} {:>12} {:>18} {:>18}".format(player["player"].get_name(), "₱" + str(player["bet"]), str(player["numbers"][0]) +  " " + str(player["numbers"][1]) + " " + str(player["numbers"][2]), "X"))
        print("-"*65)

def main():
    game = Game()

    for name in contestant_names:
        player = Player(name, 200)
        
        game.add_player(player, [random.randrange(MIN, MAX), random.randrange(MIN, MAX), random.randrange(MIN, MAX)], random.randrange(10, 100))
    
    PLAYER = Player(NAME, MONEY)

    print("Name: {}\nMoney: ₱{}\nCredit Pin: {}".format(PLAYER.get_name(), PLAYER.get_money(), filter_pin(CREDIT_PIN)))

    print() 

    FIRST = int(input("First Number [{} - {}]: ".format(MIN, MAX)))

    while FIRST <= 0 or FIRST > MAX:
        FIRST = int(input("First Number [{} - {}]: ".format(MIN, MAX)))

    SECOND = int(input("Second Number [{} - {}]: ".format(MIN, MAX)))

    while SECOND <= 0 or SECOND > MAX:
        SECOND = int(input("Second Number [{} - {}]: ".format(MIN, MAX)))

    THIRD = int(input("Third Number [{} - {}]: ".format(MIN, MAX)))

    while THIRD <= 0 or THIRD > MAX:
        THIRD = int(input("Third Number [{} - {}]: ".format(MIN, MAX)))

    BET = int(input("Enter your bet [₱{} - ₱{}]: ₱".format(game.get_min_bet(), MONEY)))

    while BET > MONEY or BET < game.get_min_bet():
        BET = int(input("Enter your bet [₱{} - ₱{}]: ₱".format(game.get_min_bet(), MONEY)))

    game.add_player(PLAYER, [FIRST, SECOND, THIRD], BET)

    print("")
    game.run()

if __name__ == "__main__":
    main()