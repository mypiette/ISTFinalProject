# coding: utf-8

""" Decision Helper: The purpose of this module is to aid users in making a decision between the choices they provide. 
The idea is that a user will input choices and then decide what sort of choice they would like help with, i.e. fully random, 
psuedo random, or even by playing a game with the program. By the end, the user will have an answer...or will decide to use 
the module again and again util it returns the desired answered ;) """

__author__ = "Marie Piette"
__copyright__ = "Copyright 2017, Decision Helper"
__credits__ = ["Marie Piette"]
__version__ = "1.0.0"
__email__ = "marie.piette@cgu.edu"
__status__ = "Production"
#
# Decision Helper
# Filename: hw0pr1.py
# Name: Marie Piette
# Problem description: Rock Paper Scissors with a Computer
# Solution Summary: Identify the user's text as the 3 options, randomly choose option for computer, compare choices
# While comparing, identify which scenario/use case is correct and personalize the output



import random          # imports the library named random for computer options, and will be the main focus of this module


# print("Please type 'rps()' to proceed.") #to guide user



def numOfChoices():
    """ a function that simply prints the menu for the number of choices to be used """
    print()
    print("Please select how many choices you are offering:")
    print("(1) Two Choices")
    print("(2) Three Choices")
    print("(3) More than Three Choices")
    print("(9) Quit")
    print()

def kindOfDecisionsTwoChoices():
    """ a function that simply prints the menu for the types of decisions that can be made """
    print()
    print("Please choose what type of Decision Helper function you would like to use:")
    print("(1) Flip a Coin")
    print("(2) Rock, Paper, Scissors")
    print("(3) Rock, Paper, Scissors, Lizard, Spock")
    print("(4) Random among random")
    #print("(4) Tic Tac Toe/chess with user")
    #print("(5) Tic Tac Toe/chess with 2 computers")
    print("(9) Quit")
    print()

def kindOfDecisionsThreeChoices():
    """ a function that simply prints the menu for the types of decisions that can be made """
    print()
    print("(1) Random")
    print("(2) Coin Flips") #see website
    print("(3) Matches in 4")#??
    print("(4) Shuffle among choices") # shuffle and designate what place in the list and that's the choice
    print("(5) Random among random")
    #print("(4) Tic Tac Toe/chess between computer")
    print("(9) Quit")
    print()

def kindOfDecisionMoreThanThreeChoices():
    """ a function that simply prints the menu for the types of decisions that can be made """
    print()
    print("(1) Random")
    print("(2) Coin Flips with decision")
    print("(3) Shuffle among cards") #assign choices to a set of cards and then choose a random card and itll correspond to whatever choices??
    print("(4) Psuedo Random through chosen Probabilities")
    print("(5) Random among random")
    #print("(4) Tic Tac Toe/chess between computer")
    print("(9) Quit")
    print()

def printList(L):
    """ prints the list line by line"""
    for x in L:
        print(x)


def rockPaperScissors2(L):
    """ this plays a game of rock-paper-scissors
        (or a variant of that game ...)
        input L: list of 2 choices
        outputs: returns winning choice
    """
    
    print("Now we will play 1 round of 'Rock, Paper, Scissors'\n")
    print("Out of your two choices below, which one would you like to represent? " + 
    "If you enter 'random' then the Decision Helper will randomly decide which one you will play for.")
    printList(L)
    print()
    userChoiceRep = input() # user chooses which one they are playing for
    dhChoiceRep = ""

    if userChoiceRep == 'random' or userChoiceRep == 'Random'or userChoiceRep == 'RANDOM':
        userChoiceRep = random.choice(L) #decision helper will choose which one the user will represent
        print("Since you chose 'random', the Decision Helper decided that you would represent:")
        print("\"",userChoiceRep,"\"")
    
    if userChoiceRep == L[0]: #the computer will then be the other choice
        dhChoiceRep = L[1]
    elif userChoiceRep == L[1]:
        dhChoiceRep = L[0]
    else:
        print("I'm sorry, ",userChoiceRep,"is not one of the choices offered.")
        print("Please try again")
        rockPaperScissors2(L)
        # print("SILLY MARIE FIGURE IT OUT")


    print()
    print("You are now playing: ", userChoiceRep)
    print("Decision Helper is now playing: ", dhChoiceRep)

    print()
    print("With that decided...")
    
    user = input("Choose your weapon: rock, paper, or scissors \n") # has user choose weapon
    comp = random.choice( ['rock','paper','scissors'] ) #randomly chooses one of the 3
    print() # added spacing

    print('the User (You) chose:', user) # identify "inputs"
    print('the Decision Helper chose:', comp)
    print()

    if user == 'rock' or user =='Rock': #two options, just in case user uses caps # User chooses Rock
        if comp == 'paper' or comp == 'Paper': 
            print("'" + comp + "' covers '" + user +"'. So Decision Helper wins!") # added the reasoning of why who won # used the real inputs for debuggin/just in case mistypes
            return dhChoiceRep
        
        elif comp == 'scissors' or comp == 'Scissors':
            print( "'" + user + "' crushes '" + comp + "'. So you win!")
            return userChoiceRep

        else:
            print( "We both put '" + comp + "' so we tie!") # so that i can easily copy and paste 
            print("Because we tied with '",comp, "' we will play again!")
            print()
            rockPaperScissors2(L)

            # print("SILLY MARIE - PUT IN A WHILE LOOP TO HANDLE TIES AND BREAKS FOR ROCK")

    elif user == 'paper' or user =='Paper':  #User chooses Paper
        if comp == 'rock' or comp == 'Rock':
            print("'" + user + "' covers '" + comp +"'. So you win!") 
            return userChoiceRep
            
        elif comp == 'scissors' or comp == 'Scissors':
            print( "'" + comp + "' cuts '" + user + "'. So Decision Helper wins!")
            return dhChoiceRep              

        else:
            print( "We both put '" + comp + "' so we tie!") 
            print("Because we tied with '",comp, "' we will play again!")
            print()
            rockPaperScissors2(L)
            
    elif user == 'scissors' or user =='Scissors': #User chooses Scissors
        if comp == 'rock' or comp == 'Rock':
            print("'" + comp + "' crushes '" + user +"'. So Decision Helper wins!") 
            return dhChoiceRep
            
        elif comp == 'paper' or comp == 'Paper':
            print( "'" + user + "' cuts '" + comp + "'. So you win!")
            return userChoiceRep

        else:
            print( "We both chose '" + comp + "' so we tie!")
            print("Because we tied with '",comp, "' we will play again!")
            print()
            rockPaperScissors2(L)
               
    else:
        print("I'm sorry, '" + user + "' is not one of the three options. Please try again.") #give the option to try again after mistyping
        rockPaperScissors2(L)
        # print("SILLY MARIE - PUT IN A WHILE LOOP TO HANDLE BAD USER TYPING")
        
def rockPaperScissorsLizardSpock2(L):
    """ this plays a game of rock-paper-scissors-lizard-spock
        input L: list of 2 choices
        outputs: returns winning choice
    """
    
    print("Now we will play 1 round of 'Rock, Paper, Scissors, Lizard, Spock'\n")
    print("Out of your two choices below, which one would you like to represent? " + 
    "If you enter 'random' then the Decision Helper will randomly decide which one you will play for.")
    printList(L)
    print()
    userChoiceRep = input() # user chooses which one they are playing for
    dhChoiceRep = ""

    if userChoiceRep == 'random' or userChoiceRep == 'Random'or userChoiceRep == 'RANDOM':
        userChoiceRep = random.choice(L) #decision helper will choose which one the user will represent
        print("Since you chose 'random', the Decision Helper decided that you would represent:")
        print("\"",userChoiceRep,"\"")
    
    if userChoiceRep == L[0]: #the computer will then be the other choice
        dhChoiceRep = L[1]
    elif userChoiceRep == L[1]:
        dhChoiceRep = L[0]
    else:
        print("I'm sorry, ",userChoiceRep,"is not one of the choices offered.")
        print("Please try again")
        rockPaperScissorsLizardSpock2(L)


    print()
    print("You are now playing: ", userChoiceRep)
    print("Decision Helper is now playing: ", dhChoiceRep)

    print()
    print("With that decided...")
    
    user = input("Choose your weapon: rock, paper, scissors, lizard, spock \n") # has user choose weapon
    comp = random.choice( ['rock','paper','scissors','lizard','spock'] ) #randomly chooses one of the 3
    print()

    print('the User (You) chose:', user) # identify "inputs"
    print('the Decision Helper chose:', comp)
    print()

    if user == 'rock' or user =='Rock': #two options, just in case user uses caps # User chooses Rock
        if comp == 'paper' or comp == 'Paper': 
            print("'" + comp + "' covers '" + user +"'. So Decision Helper wins!") # added the reasoning of why who won # used the real inputs for debuggin/just in case mistypes
            return dhChoiceRep
        
        elif comp == 'lizard' or comp == 'Lizard': #rock crushes lizard
            print( "'" + user + "' crushes '" + comp + "'. So you win!")
            return userChoiceRep
        
        elif comp == 'spock' or comp == 'Spock': #spock vaporizes rock
            print("'" + comp + "' vaporizes '" + user +"'. So Decision Helper wins!")
            return dhChoiceRep
        
        elif comp == 'scissors' or comp == 'Scissors': #and as always, rock crushes scissors
            print( "'" + user + "' crushes '" + comp + "'. So you win!")
            return userChoiceRep

        else:
            print( "We both put '" + comp + "' so we tie!") # so that i can easily copy and paste if the tie happens
            print("Because we tied with '",comp, "' we will play again!")
            print()
            rockPaperScissorsLizardSpock2(L)

    elif user == 'paper' or user =='Paper':  #User chooses Paper
        if comp == 'rock' or comp == 'Rock':    #paper covers rock
            print("'" + user + "' covers '" + comp +"'. So you win!") 
            return userChoiceRep
            
        elif comp == 'scissors' or comp == 'Scissors': #scissors cuts paper
            print( "'" + comp + "' cuts '" + user + "'. So Decision Helper wins!")
            return dhChoiceRep        

        elif comp == 'lizard' or comp == 'Lizard': #lizard eats paper
            print( "'" + comp + "' eats '" + user + "'. So Decision Helper wins!")
            return dhChoiceRep   

        elif comp == 'spock' or comp == 'Spock': #paper disproves spock
            print("'" + user + "' disproves '" + comp +"'. So you win!") 
            return userChoiceRep

        else:
            print( "We both put '" + comp + "' so we tie!") 
            print("Because we tied with '",comp, "' we will play again!")
            print()
            rockPaperScissorsLizardSpock2(L)
            
    elif user == 'scissors' or user =='Scissors': #User chooses Scissors
        if comp == 'rock' or comp == 'Rock': #rock crushes scissors
            print("'" + comp + "' crushes '" + user +"'. So Decision Helper wins!") 
            return dhChoiceRep
            
        elif comp == 'paper' or comp == 'Paper': #scissors cuts paper
            print( "'" + user + "' cuts '" + comp + "'. So you win!")
            return userChoiceRep

        elif comp == 'spock' or comp == 'Spock': #spock smashes scissors
            print("'" + comp + "' smashes '" + user +"'. So Decision Helper wins!") 
            return dhChoiceRep

        elif comp == 'lizard' or comp == 'Lizard': #scissors decapitates lizard
            print( "'" + user + "' decapitates '" + comp + "'. So you win!")
            return userChoiceRep

        else:
            print( "We both chose '" + comp + "' so we tie!")
            print("Because we tied with '",comp, "' we will play again!")
            print()
            rockPaperScissorsLizardSpock2(L)

    elif user == 'lizard' or user =='Lizard': #User chooses Lizard
        if comp == 'rock' or comp == 'Rock': #rock crushes lizard
            print("'" + comp + "' crushes '" + user +"'. So Decision Helper wins!") 
            return dhChoiceRep
            
        elif comp == 'spock' or comp == 'Spock': #lizard poisons spock
            print( "'" + user + "' poisons '" + comp + "'. So you win!")
            return userChoiceRep

        elif comp == 'scissors' or comp == 'Scissors': #scissors decapitates lizard
            print("'" + comp + "' decapitates '" + user +"'. So Decision Helper wins!") 
            return dhChoiceRep

        elif comp == 'paper' or comp == 'Paper': #Lizard eats paper
            print( "'" + user + "' eats '" + comp + "'. So you win!")
            return userChoiceRep

        else:
            print( "We both chose '" + comp + "' so we tie!")
            print("Because we tied with '",comp, "' we will play again!")
            print()
            rockPaperScissorsLizardSpock2(L)

    elif user == 'spock' or user =='Spock': #User chooses Lizard
        if comp == 'lizard' or comp == 'Lizard': #lizard poisons spock
            print("'" + comp + "' poisons '" + user +"'. So Decision Helper wins!") 
            return dhChoiceRep
            
        elif comp == 'scissors' or comp == 'Scissors': #lspock smashes scissors
            print( "'" + user + "' smashes '" + comp + "'. So you win!")
            return userChoiceRep

        elif comp == 'paper' or comp == 'paper': #paper disproves spock
            print("'" + comp + "' disproves '" + user +"'. So Decision Helper wins!") 
            return dhChoiceRep

        elif comp == 'rock' or comp == 'Rock': #spock vaporizes rock
            print( "'" + user + "' vaporizes '" + comp + "'. So you win!")
            return userChoiceRep

        else:
            print( "We both chose '" + comp + "' so we tie!")
            print("Because we tied with '",comp, "' we will play again!")
            print()
            rockPaperScissorsLizardSpock2(L)

               
    else:
        print("I'm sorry, '" + user + "' is not one of the three options. Please try again.") #give the option to try again after mistyping
        rockPaperScissorsLizardSpock2(L)
   
def randomAmongRandom(L):
    """ This function takes an array list of choices and adds them to a list in multiples of a randomly chosen number between 1 and 1000.
        From that big list, it randomly decides and that's the answer
        input L: list of choices
        output: decision
    """
    # note to self - make this a more modular function - 
    # create an array of randomMultiples to match the array of given choices
    # make new list of choices with random multiples
    numOfNeededMultiples = len(L)
    multiplesList = []
    for x in range(numOfNeededMultiples): #creates list of multiples needed
        multiple = random.randrange(1,10) #uses the "randrange" function of random library to choose a random number between 0 and 1000 to have that many multiples of each choice
        multiplesList.append(multiple)
    
    print("list of multiples: ", multiplesList)

    choicesToMultiple = [] #create list of multiples to match with choices
    for x in multiplesList: #for the each value of multiplesList
        print("x: ", x)
        while x > 0 and len(L) >= 1:
            # print("L[0] = ", L[0]) #testing
            choicesToMultiple.append(L[0])
            # print("new choicesToMultiple: ", choicesToMultiple) #testing
            x = x - 1
        L = L[1:]
        # print("L: ", L) #testing
                

    print("The final list of choices, with the random multiple of each choice:", choicesToMultiple)

    #original code when i was making it specifically 2 choices - changed and adapted for more than that
        # randomMultiple1 = random.randrange(0,10) #uses the "randrange" function of random library choose a random number between 0 and 1000 to have that many multiples of first choice
        # randomMultiple2 = random.randrange(0,10) 
        # print("randomMultiple1: ", randomMultiple1) #testing
        # print("randomMultiple2: ", randomMultiple2)

        # twoChoicesToMultiple = [""] #new list to have as many replicates of choices as randomly decided
        # for x in range(randomMultiple1):
        #     twoChoicesToMultiple.append(choices[0]) #add choice 1 to new list

        # for x in range(randomMultiple2)
        #     twoChoicesToMultiple.append(choices[1]) #add choice 2 to new list

    # print("The Decision Helper created a list with ", randomMultiple1, "representation(s) of your first choice: ", choices[0])
    # print("The Decision Helper created a list with ", randomMultiple2, "representation(s) of your first choice: ", choices[1])
    rardecision = random.choice(choicesToMultiple) #randomly choose among the new list of random number of choices to add a level of randomness
    # print("The Decision Helper then randomly chose: ", decision)
    return rardecision

def coinFlips3(L): 
    """play an orchestrated game of flipping coins for some 'random' calibration
        input L: list of choices
    """

    print("You'll have to choose (twice) which combination you want to live and which choice they represent")
    reps1 = input("Choose between  HH, HT, TH, or TT with H == heads and T == Tails") #reps1 = representing first choice
    if reps1 == "HH" or reps1 == "hh":
        reps2 = input("Choose a second combination between HT, TH, or TT with H == heads and T == Tails")
        if reps2 == "HT":
            comp = random.choose("TH", "TT")
        elif reps2 == "TH":
            comp = random.choose("HT", "TT")
        elif reps2 == "TT":
            comp = random.choose("HT", "TH")
        else:
            print("DO SOMETHING WITH THE MIstYPE SILLY")
    
    elif reps1 == "HT" or reps1 == "ht":
        reps2 = input("Choose a second combination between HH, TH, or TT with H == heads and T == Tails")
        if reps2 == "HH":
            comp = random.choose("TH", "TT")
        elif reps2 == "TH":
            comp = random.choose("HH", "TT")
        elif reps2 == "TT":
            comp = random.choose("HH", "TH")
            
    elif reps1 == "TH" or reps1 == "th":
        reps2 = input("Choose a second combination between HH, HT, or TT with H == heads and T == Tails")
        if reps2 == "HH":
            comp = random.choose("HT", "TH")
        elif reps2 == "HT":
            comp = random.choose("HH", "TT")
        elif reps2 == "TT":
            comp = random.choose("HH", "HT")
    elif reps1 == "TT" or reps1 == "tt":
        reps2 = input("Choose a second combination between HH, HT, or TH with H == heads and T == Tails")
        if reps2 == "HH":
            comp = random.choose("HT", "TH")
        elif reps2 == "HT":
            comp = random.choose("HH", "TT")
        elif reps2 == "TT":
            comp = random.choose("HH", "HT")
    else:
        print("I didn't understand your answer. Please try again!")
        coinFlips3(L)
        
    

def main():
    """ the main user-interaction loop """

    print("Hello! Welcome to the Decision Helper, where we try to help you narrow down your choices. First...")
    choices = []
    kd = 0 #kind of decision
    
    while True:
        numOfChoices()
        numChoice = input()

        try:
            numChoice = int(numChoice)   # make into an int!
        except:
            print("I didn't understand your input! Continuting...")
            continue
        
        if numChoice == 1:
            print()
            print("You've chosen option 1) Two Choices") 
            print("Please enter your two choices.")
            choices = ["", ""]
            choices[0] = input()
            choices[1] = input()
            print()
            print("Great! Your choices were: ")
            printList(choices)
            print()
            print("Now that you've entered your choices...")
            kindOfDecisionsTwoChoices()
            kd = input()
            try:
                kd = int(kd)   # make into an int!
            except:
                print("I didn't understand your input! Continuting...")
                continue     
            
            if kd == 1: #flip a coin == random between 2 choices
                decision = random.choice(choices)
                print()
                print("You chose option 1) 'Random' and the Decision Helper decided: ")
                print("\"", decision, "\"")
                print("Hope that helped!")

            elif kd == 2:
                print()
                print("You chose option 2) Rock, Paper, Scissors")
                decision = rockPaperScissors2(choices)
                print("And therefore, the decision is: \"", decision, "\"")
                print()
                print("Would you like to play Rock, Paper, Scissors again with the same choices? Y or N") #play rock paper scissors again with same choices
                rpsAgain = input()
                print()
                if rpsAgain == 'Y' or rpsAgain == 'y' or rpsAgain == 'Yes':
                    print("Here we go again!")
                    decision = rockPaperScissors2(choices)
                    print("And therefore, the decision is: \"", decision, "\"")
                    print()
                elif rpsAgain == 'N' or rpsAgain == 'n' or rpsAgain == 'No' or rpsAgain == 'no':
                    print("Ok no problem!")
                else:
                    print("I didn't understand your input! Continuting...")
                    continue 

                print("Hope that helped!")

            elif kd == 3:
                print()
                print("You chose option 3) Rock, Paper, Scissors, Lizard, Spock")
                decision = rockPaperScissorsLizardSpock2(choices)
                print("And therefore, the decision is: \"", decision, "\"")
                print()

                while True: #keep asking until they say no
                    print("Would you like to play Rock, Paper, Scissors, Lizard Spock again with the same choices? Y or N") #play rock paper scissors again with same choices
                    rpslsAgain = input()
                    print()
                    if rpslsAgain == 'Y' or rpslsAgain == 'y' or rpslsAgain == 'Yes' or rpslsAgain == 'yes':
                        print("Here we go again!")
                        decision = rockPaperScissorsLizardSpock2(choices)
                        print("And therefore, the decision is: \"", decision, "\"")
                        print()
                        return True
                    elif rpslsAgain == 'N' or rpslsAgain == 'n' or rpslsAgain == 'No' or rpslsAgain == 'no':
                        print("Ok no problem!")
                        return False
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 

                print("Hope that helped!")
            
            elif kd == 4:
                print()
                print("You chose option 4) 'Random among random'. This means that Decision Helper will create a list of a random multiple (between 0 and 1000) " + 
                "of each choice and then choose among said list of choices.") 
                decision = randomAmongRandom(choices)
                print("Decision Helper decided: ")
                print("\"", decision, "\"")
                while True: #keep asking until they say no
                    print("Would you like to play \"Random among random\" again with the same choices? Y or N") #play rock paper scissors again with same choices
                    randOfRandAgain = input()
                    print()
                    if randOfRandAgain == 'Y' or randOfRandAgain == 'y' or randOfRandAgain == 'Yes' or randOfRandAgain == 'yes':
                        print("Here we go again!")
                        decision = randomAmongRandom(choices)
                        print("And therefore, the decision is: \"", decision, "\"")
                        print()
                        continue
                    elif randOfRandAgain == 'N' or randOfRandAgain == 'n' or randOfRandAgain == 'No' or randOfRandAgain == 'no':
                        print("Ok no problem!")
                        break
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 
                
                print("Hope that helped!")

        elif numChoice == 2:
            print()
            print("You've chosen option 2) Three Choices") 
            print("Please enter your three choices.")
            choices = ["", "", ""]
            choices[0] = input()
            choices[1] = input()
            choices[2] = input()
            print()
            print("Great! Your choices were: ")
            printList(choices)
            print()
            print("Now that you've entered your choices...")
            kindOfDecisionsTwoChoices()
            try:
                kd = int(kd)   # make into an int!
            except:
                print("I didn't understand your input! Continuting...")
                continue     

            if kd == 1: #flip a coin == random between 2 choices
                decision = random.choice(choices)
                print()
                print("You chose option 1) 'Random' and the Decision Helper decided: ")
                print("\"", decision, "\"")
                print("Hope that helped!")

            elif kd ==2:
                print("You chose option 2) Coin Flips. This means you'll play a round of coin flips that is meant for 3 choices.")
                #method
            




def kindOfDecisionsThreeChoices():
    """ a function that simply prints the menu for the types of decisions that can be made """
    print()
    print("(1) Random")
    print("(2) Coin Flips") #see website
    print("(3) Matches in 4")#??
    print("(4) Shuffle among choices") # shuffle and designate what place in the list and that's the choice
    print("(5) Random among random")
    #print("(4) Tic Tac Toe/chess between computer")
    print("(9) Quit")
    print()
            

        elif numChoice == 9:
            break
            
        else:
            print("silly marie, you need do something!!!")

        print()
        print("Are you done deciding? Y or N")
        doneAns = input()
        if doneAns == 'N' or doneAns == 'n' or doneAns == 'no':
            print("\nOk, another round it is!")
            continue
        else:
            print("\nCongrats! Have a good one :)")
            break

        


    


















#ORIGINAL COPY AND PASTE FORM HW0 LAB
# # coding: utf-8
# #
# # hw0pr2.py
# #

# """ 
# Notes on this rps function:


# """
# import time            # includes a library named time
# import random        # includes a library named random


# def rps():
#     """ this plays a game of rock-paper-scissors
#         (or a variant of that game ...)
#         inputs: no inputs    (prompted text doesn't count as input)
#         outputs: no outputs  (printing doesn't count as output)
#     """
#     name = input('Hi...what is your name? ')
#     print()
#     print("Hmmm...")
#     print()

#     if name == 'Geoff' or name == 'Colleen':
#         print('I\'m "offline" Try later.')
        
#     elif name == 'Zach':
#         print('Zach!  Efron? Quinto? Galifianakis?')
#         time.sleep(1)
#         print('No?')
#         time.sleep(1)
#         print('Meh.')
        
#     else:
#         print('Welcome,', name)
#         my_choice = random.choice( ['rock','paper','scissors'] )
#         print('By the way, I choose ', my_choice)