from random import randint

class player:
    player_name = "Bot"
    player_prizes = "10"
    player_money = "100$"
    def set_player_details(self,name, prizes, money):

        self.player_name = name
        self.player_prizes = prizes
        self.player_money = money

    def get_player_details(self):

        print("Name:{}\nPrizes:{}\nMoney:{}".format(self.player_name, self.player_prizes, self.player_money))



class lucky_number_generator:

    def generate_number(self):
        self.lucky_number = randint(1, 5)
        #return lucky_number



class Game(player, lucky_number_generator):

    def __init__(self):
        pass


GameObj = Game()



'''def game_play(self):
        print("game staarted")
        pass
        ''''''
        #print("Enter Your Choice: ")
        #user_choice = int(input())

        if lucky_number_generatorobj.generate_number()== user_choice :
            print("Correct Guess")'''

'''player = Game()
#Game.get_player_details()
Game.set_player_details()
Game.generate_number()
Game.game_play()'''

Choice = True
while Choice == True:
                print("(1) Set Up New Player\n"
                      "(2) Guess A Prize \n"
                      "(3) What Have I Won So Far?\n"
                      "(4) Display Game Help\n"
                      "(5) Exit Game\n")
                choice = int(input("Select an option : "))

                if choice == 1:
                    print("Enter Player details")
                    name = input("Enter player name :" )
                    prizes = int(input("Enter No. of Prizes : "))
                    money = float(input("Enter Total money player has : "))
                    GameObj.set_player_details(name,prizes,money)
                    continue

                    #playerobj = player(player_name, player_prizes, player_money )'''

                elif choice == 2:
                    '''print ("Do You want to enter Game - Press Y to Continue or No to Main Menu ")
                    choice_for_game = str(input())
                    if choice_for_game  == "Y" or "y":
                        print("Lets Start the game")
                        break
                    elif choice_for_game == "N" or "n":
                        continue
                    else:
                        print ("Enter a valid response")'''
                    print("Lets Roll the ball")
                    print("Guess a Number Based Upon the List")
                    Guess_Number = int(input())
                    GameObj.generate_number()

                    if Guess_Number == GameObj.lucky_number:
                        print("You Selected Number {} and LuckyNumberGenerated is {}".format(Guess_Number,GameObj.lucky_number))
                        print("You Won",Guess_Number*10,"$")
                        GameObj.player_money += Guess_Number*10-Guess_Number
                        print("New Score\n",GameObj.get_player_details())
                        if Guess_Number == 1:
                            print("And You-Won a Pen")
                            break
                        elif Guess_Number == 2:
                            print("And You-Won a Book")
                            break
                        elif Guess_Number == 3:
                            print("And You-Won a DVD")
                            break
                        elif Guess_Number == 4:
                            print("And You-Won a Mouse")
                            break
                        elif Guess_Number == 5:
                            print("And You-Won a Keyboard")
                            break
                    else:

                        GameObj.player_money-=Guess_Number
                        print("New Score\n",GameObj.get_player_details())

                        break



                elif choice == 3:
                        GameObj.get_player_details()
                        #print("You have won so far {} prizes and {}'$' as money",format(GameObj.player_prizes,GameObj.player_money))


                elif choice == 4:
                    print("Help center")


                elif choice == 5:
                        exit(0)


                else:
                    print("Enter a Valid Choice")
                    continue

