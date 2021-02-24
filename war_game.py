import random
import sys

class deck():
    suits = ["H","D","S","C"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]  
    allCards = []

    # method_1

    def __init__(self):
       for suit in self.suits:
            for rank in self.ranks:
                self.allCards.append(suit + rank)

    # method_2
    """
    def __init__(self,SUITE,RANK):
        self.suite = SUITE   
        self.rank = RANK
        self.allCards = []
        for suite in SUITE:
            for rank in RANK:
                self.allCards.append(suite+rank)
        print(self.allCards)
    """

    def shuffle_cards(self):
        random.shuffle(self.allCards)
     

    def splitting_cards(self):
        middle = len(self.allCards) // 2

        first_list = self.allCards[:middle]
        second_list = self.allCards[middle:]
        
        return first_list , second_list
    

class Hand():
    def adding_cards(self,new_Cards,gain_Cards):
        new_Cards.append(gain_Cards)
        return new_Cards

    def removing_cards(self,new_Cards,lost_Cards):
        return new_Cards[len(lost_Cards):]

class Player(Hand):
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    count = 0
    def __init__(self,player1_Cards,master_Cards):
        self.player1_cards = player1_Cards
        self.master_cards = master_Cards
        self.name = input("Enter your Name:- ")
        print(" ")
        print(self.name + " ! " + "*** Welcome to the Cards_Game (Teen_patti) *** ")
        print(" ")

    def wish(self):
        x = input("Do you want to continue the Game(Y/N) :- ")
        if x.lower() == "y":
            self.actual()
        else:
            print("Oops ! You exited the Game")
            exit()


    def rank_Index(self,value):
        count = 0
        for i in self.ranks:
            if (i == value):
                return count
            count = count + 1
        return -1

    def actual(self):
        Round1 = 1
        while( (len(self.player1_cards)) > 0 and ( (len(self.master_cards)) > 0 )):
            player1_rank = self.player1_cards[0][1:]
            master_rank = self.master_cards[0][1:]
            # player1_suit = self.player1_cards[0][0]
            # master_suit = self.master_cards[0][0]
            print("")
            print(" Round :- ", Round1)
            Round1 = Round1 + 1
            print(" player1_cards ",self.player1_cards[0], " master_Cards ",self.master_cards[0])
            print(player1_rank,master_rank)

             #player1rank
            if(self.rank_Index(player1_rank) > self.rank_Index(master_rank)):
                print(self.name + " Won this Round ")
                self.player1_cards = super().adding_cards(self.player1_cards,self.master_cards[0])
                self.player1_cards = super().adding_cards(self.player1_cards,self.player1_cards[0])
                self.master_cards = super().removing_cards(self.master_cards,[self.master_cards[0]])
                self.player1_cards = super().removing_cards(self.player1_cards,[self.player1_cards[0]])
                print(self.name + " present_Cards are :- ", len(self.player1_cards))
                print("master_cards:- ", len(self.master_cards))

             #masterrank

            elif (self.rank_Index(player1_rank) < self.rank_Index(master_rank)):
                print(" Master " + " Won this Round ")
                self.master_cards = super().adding_cards(self.master_cards,self.player1_cards[0])
                self.master_cards = super().adding_cards(self.master_cards,self.master_cards[0])
                self.player1_cards = super().removing_cards(self.player1_cards,[self.player1_cards[0]])
                self.master_cards = super().removing_cards(self.master_cards,[self.master_cards[0]])
                print(self.name + " present_Cards are :- ", len(self.player1_cards))
                print(" master_Cards:- ", len(self.master_cards))
            else:
                print(" ****** ITS A WAR ****** ")
                if(len(self.player1_cards) < 5 and len(self.master_cards) < 5):
                    print("its a Tie")
                    sys.exit()
                if len(self.player1_cards) < 5:
                    print("master won the Game")
                    sys.exit()
                if len(self.master_cards) < 5:
                    print(self.name +" won the Game ")
                    sys.exit()
                player1_rank = self.player1_cards[4][1:]
                master_rank = self.master_cards[4][1:]
                    
                print(player1_rank,master_rank)

                    #player1rank

                if(self.rank_Index(player1_rank) > self.rank_Index(master_rank)):
                    print(self.name + " Won this Round ")
                    for i in range(0,5):
                        self.player1_cards = super().adding_cards(self.player1_cards,self.master_cards[i])
                        self.player1_cards = super().adding_cards(self.player1_cards,self.player1_cards[i])
                    for i in range(0,5):   
                        self.master_cards = super().removing_cards(self.master_cards,[self.master_cards[0]])
                        self.player1_cards = super().removing_cards(self.player1_cards,[self.player1_cards[0]])
                        print(self.name + "present_Cards :- ", len(self.player1_cards))
                        print("master_Cards:- ", len(self.master_cards))

                    #masterrank
                elif (self.rank_Index(player1_rank) < self.rank_Index(master_rank)):
                    print("Master" + " Won this Round")
                    for i in range(0,5):
                        self.master_cards = super().adding_cards(self.master_cards,self.player1_cards[i])
                        self.master_cards = super().adding_cards(self.master_cards,self.master_cards[i])
                    for i in range(0,5):   
                        self.player1_cards = super().removing_cards(self.player1_cards,[self.player1_cards[0]])
                        self.master_cards = super().removing_cards(self.master_cards,[self.master_cards[0]])
                        print(self.name + " present_Cards are :- ", len(self.player1_cards))
                        print("master_Cards:- ", len(self.master_cards))

                else:
                    print("______ SECOND TIME WAR ______ ")
                    print(" Ignore Double Wars & Proceed further..... ")
                    self.player1_cards = super().removing_cards(self.player1_cards,[self.player1_cards[0]])
                    self.master_cards = super().removing_cards(self.master_cards,[self.master_cards[0]])


        if(len(self.player1_cards) == 0):
            print(" ... Master Won the Game ...")
        else:
            print (self.name + " Won the Game ")


deck_obj = deck()
deck_obj.shuffle_cards()
splitted_Cards = deck_obj.splitting_cards()

player_obj = Player(splitted_Cards[0],splitted_Cards[1])
player_obj.wish()