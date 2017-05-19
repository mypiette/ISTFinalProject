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


print("Please type 'Start()' to proceed.") #to guide user



def numOfChoices():
    """ a function that simply prints the menu for the number of choices to be used """
    print()
    print("Please select how many choices you are offering:")
    print("(1) Two Choices")
    print("(2) Three Choices")
    print("(3) More Than Three Choices")
    print("(9) Quit")
    print()

def kindOfDecisionsTwoChoices():
    """ a function that simply prints the menu for the types of decisions that can be made """
    print()
    print("Please choose what type of Decision Helper function you would like to use:")
    print("(1) Flip a Coin")
    print("(2) Rock, Paper, Scissors")
    print("(3) Rock, Paper, Scissors, Lizard, Spock")
    print("(4) Random among random") #random among probabilities
    #print("(4) Tic Tac Toe/chess with user")
    #print("(5) Tic Tac Toe/chess with 2 computers")
    print("(9) Quit")
    print()

def kindOfDecisionsThreeChoices():
    """ a function that simply prints the menu for the types of decisions that can be made """
    print()
    print("Please choose what type of Decision Helper function you would like to use:")
    print("(1) Random")
    print("(2) Coin Flips")
    print("(3) Shuffle among choices") # shuffle and designate what place in the list and that's the choice
    print("(4) Random among random")
    # print("(3) Matches in 4 - TBD")# i have zero memory of what this function was going to be haha
    #print("(4) Tic Tac Toe/chess between computer") #if i have the time
    print("(9) Quit")
    print()

def kindOfDecisionMoreThanThreeChoices():
    """ a function that simply prints the menu for the types of decisions that can be made """
    print()
    print("(1) Random")
    # print("(2) Coin Flips with decision") #not sure how to do it easily with a lot of choices
    #if i have time # print("(3) Shuffle among cards") #assign choices to a set of cards and then choose a random card and itll correspond to whatever choices??
    print("(2) Shuffle among choices") #similar to 3 choices
    # print("(4) Psuedo Random through chosen Probabilities") #next time
    print("(3) Random among random")
    #print("(4) Tic Tac Toe/chess between computer")
    print("(9) Quit")
    print()


def printList(L):
    """ prints the list line by line"""
    for x in L:
        print(x)

def printListWithIndex(L):
    """ prints the list line by line"""
    for x in L:
        print(L.index(x),")", x)


def rockPaperScissors2(L):
    """ this plays a game of rock-paper-scissors
        (or a variant of that game ...)
        input L: list of 2 choices
        outputs: returns winning choice
    """

    print("Now we will play 1 round of 'Rock, Paper, Scissors'\n")
    print("Out of your two choices below, which one would you like to represent? 0 or 1" + 
    "If you enter 'random' then the Decision Helper will randomly decide which one you will play for.")
    printListWithIndex(L)
    print()
    userChoiceRepIndex = input() # user chooses which one they are playing for by the index or random
    userChoiceRep = ""
    dhChoiceRep = L[0] #make default just so none doesn't show up

    if userChoiceRepIndex == "random" or userChoiceRepIndex == "Random" or userChoiceRepIndex == "RANDOM":
        userChoiceRep = random.choice(L) #decision helper will choose which one the user will represent
        print("Since you chose 'random', the Decision Helper decided that you would represent:")
        print("\"",userChoiceRep,"\"")
    
    else:
        # try:
        userChoiceRepIndex = int(userChoiceRepIndex)   # make into an int!
        # except: #idk why its not working right now
        #     print("I didn't understand your input! Continuting...")
        #     continue
        userChoiceRep = L[userChoiceRepIndex]
        
    if userChoiceRep == L[0]: #the computer will then be the other choice
        dhChoiceRep = L[1]
    elif userChoiceRep == L[1]:
        dhChoiceRep = L[0]
    else:
        print("I'm sorry, ",userChoiceRep,"is not one of the choices offered.")
        print("Please try again")
        return "Invalid Choice"
        # continue


    print()
    print("You are now playing: ", userChoiceRep)
    print("Decision Helper is now playing: ", dhChoiceRep)

    print()
    print("With that decided...")
    
    user = input("Choose your weapon: rock, paper, or scissors \n") # has user choose weapon
    comp = random.choice( ["rock","paper","scissors"] ) #randomly chooses one of the 3
    print() # added spacing

    print('the User (You) chose:', user) # identify "inputs"
    print('the Decision Helper chose:', comp)
    print()

    if user == "rock" or user =="Rock": #two options, just in case user uses caps # User chooses Rock
        if comp == "paper" or comp == "Paper": 
            print("'" + comp + "' covers '" + user +"'. So Decision Helper wins!") # added the reasoning of why who won # used the real inputs for debuggin/just in case mistypes
            return dhChoiceRep
        
        elif comp == "scissors" or comp == "Scissors":
            print( "'" + user + "' crushes '" + comp + "'. So you win!")
            return userChoiceRep

        else:
            print( "We both put '" + comp + "' so we tie!") # so that i can easily copy and paste 
            print("Because we tied with '",comp, ", neither of us wins")
            print()
            return "No decision was made"

            # print("SILLY MARIE - PUT IN A WHILE LOOP TO HANDLE TIES AND BREAKS FOR ROCK")

    elif user == "paper" or user =="Paper":  #User chooses Paper
        if comp == "rock" or comp == "Rock":
            print("'" + user + "' covers '" + comp +"'. So you win!") 
            return userChoiceRep
            
        elif comp == "scissors" or comp == "Scissors":
            print( "'" + comp + "' cuts '" + user + "'. So Decision Helper wins!")
            return dhChoiceRep              

        else:
            print( "We both put '" + comp + "' so we tie!") 
            print("Because we tied with '",comp, "' neither of us wins")
            print()
            return "No decision was made"
            
    elif user == "scissors" or user =="Scissors": #User chooses Scissors
        if comp == "rock" or comp == "Rock":
            print("'" + comp + "' crushes '" + user +"'. So Decision Helper wins!") 
            return dhChoiceRep
            
        elif comp == "paper" or comp == "Paper":
            print( "'" + user + "' cuts '" + comp + "'. So you win!")
            return userChoiceRep

        else:
            print( "We both chose '" + comp + "' so we tie!")
            print("Because we tied with '",comp, "' neither of us wins")
            print()
            return "No decision was made"
               
    else:
        print("I'm sorry, '" + user + "' is not one of the three options. Please try again.") #give the option to try again after mistyping
        rockPaperScissors2(L)
        # print("SILLY MARIE - PUT IN A WHILE LOOP TO HANDLE BAD USER TYPING")
        
def rockPaperScissorsLizardSpock2(L):
    """ this plays a game of rock-paper-scissors-lizard-spock
        input L: list of 2 choices
        outputs: returns winning choice
        source: http://bigbangtheory.wikia.com/wiki/Rock_Paper_Scissors_Lizard_Spock
    """
    
    print("Now we will play 1 round of 'Rock, Paper, Scissors, Lizard, Spock'\n")
    print("Out of your two choices below, which one would you like to represent? " + 
    "If you enter 'random' then the Decision Helper will randomly decide which one you will play for.")
    printListWithIndex(L)
    print()
    userChoiceRepIndex = input() # user chooses which one they are playing for by the index or random
    userChoiceRep = ""
    dhChoiceRep = L[0] #make default just so none doesn't show up

    if userChoiceRepIndex == "random" or userChoiceRepIndex == "Random" or userChoiceRepIndex == "RANDOM":
        userChoiceRep = random.choice(L) #decision helper will choose which one the user will represent
        print("Since you chose 'random', the Decision Helper decided that you would represent:")
        print("\"",userChoiceRep,"\"")
    
    else:
        # try:
        userChoiceRepIndex = int(userChoiceRepIndex)   # make into an int!
        # except: #idk why its not working right now
        #     print("I didn't understand your input! Continuting...")
        #     continue
        userChoiceRep = L[userChoiceRepIndex]
        
    if userChoiceRep == L[0]: #the computer will then be the other choice
        dhChoiceRep = L[1]
    elif userChoiceRep == L[1]:
        dhChoiceRep = L[0]
    else:
        print("I'm sorry, ",userChoiceRep,"is not one of the choices offered.")
        print("Please try again")
        rockPaperScissors2(L)
        # continue



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
            print("Because we tied with '",comp, "' neither of us wins")
            print()
            return "No decision was made"

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
            print("Because we tied with '",comp, "' neither of us wins")
            print()
            return "No decision was made"
            
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
            print("Because we tied with '",comp, "' neither of us wins")
            print()
            return "No decision was made"

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
            print("Because we tied with '",comp, "' neither of us wins")
            print()
            return "No decision was made"

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
            print("Because we tied with '",comp, "' neither of us wins")
            print()
            return "No decision was made"

               
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
        multiple = random.randrange(1,57) #uses the "randrange" function of random library to choose a random number between 0 and 1000 to have that many multiples of each choice
        multiplesList.append(multiple)
    
    print("list of multiples: ")
    printList(multiplesList)
    print()

    choicesToMultiple = [] #create list of multiples to match with choices
    for x in multiplesList: #for the each value of multiplesList
        # print("x: ", x)
        while x > 0 and len(L) >= 1:
            # print("L[0] = ", L[0]) #testing
            choicesToMultiple.append(L[0])
            # print("new choicesToMultiple: ", choicesToMultiple) #testing
            x = x - 1
        L = L[1:]
        # print("L: ", L) #testing
                

    print("The final list of choices, with the random multiple of each choice:")
    print(choicesToMultiple)

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
    # print("The Decision Helper then randomly chose: ", rardecision)
    return rardecision

def coinFlips3(L): 
    """play an orchestrated game of flipping coins for some 'random' calibration
        input L: list of choices
        source: https://www.quora.com/How-do-you-decide-the-winner-among-3-people-with-an-equal-probability-by-tossing-a-fair-coin
    """
    userCoinChoices = []
    print("You'll have to choose (twice) which combination you want to win and which choice they represent")
    reps1 = input("Choose between  HH, HT, TH, or TT with H == heads and T == Tails \n") #reps1 = representing first choice
    print()
    leftOverList = []
    if reps1 == "HH" or reps1 == "hh":
        reps2 = input("Choose a second combination between HT, TH, or TT with H == heads and T == Tails \n")
        print()
        if reps2 == "HT" or reps2 == "hh":
            leftOverList = ["TH", "TT"]
            comp = random.choice(leftOverList)
        elif reps2 == "TH" or reps2 == "th":
            leftOverList = ["HT", "TT"]
            comp = random.choice(leftOverList)
        elif reps2 == "TT" or reps2 == "tt":
            leftOverList = ["HT", "TH"]
            comp = random.choice(leftOverList)
        else:
            print("I didn't understand your answer. Please try again!")
            coinFlips3(L)
    
    elif reps1 == "HT" or reps1 == "ht":
        reps2 = input("Choose a second combination between HH, TH, or TT with H == heads and T == Tails \n")
        print()
        if reps2 == "HH" or reps2 == "hh":
            leftOverList = ["TH", "TT"]
            comp = random.choice(leftOverList)
        elif reps2 == "TH" or reps2 == "th":
            leftOverList = ["HH", "TT"]
            comp = random.choice(leftOverList)
        elif reps2 == "TT" or reps2 == "tt":
            leftOverList = ["HH", "TH"]
            comp = random.choice(leftOverList)
        else:
            print("I didn't understand your answer. Please try again!")
            coinFlips3(L)
            
    elif reps1 == "TH" or reps1 == "th":
        reps2 = input("Choose a second combination between HH, HT, or TT with H == heads and T == Tails \n")
        print()
        if reps2 == "HH" or reps2 == "hh":
            leftOverList = ["HT", "TH"]
            comp = random.choice(leftOverList)
        elif reps2 == "HT" or reps2 == "ht":
            leftOverList = ["HH", "TT"]
            comp = random.choice(leftOverList)
        elif reps2 == "TT" or reps2 == "tt":
            leftOverList = ["HH", "HT"]
            comp = random.choice(leftOverList)
        else:
            print("I didn't understand your answer. Please try again!")
            coinFlips3(L)

    elif reps1 == "TT" or reps1 == "tt":
        reps2 = input("Choose a second combination between HH, HT, or TH with H == heads and T == Tails \n")
        print()
        if reps2 == "HH" or reps2 == "hh":
            leftOverList = ["HT", "TH"]
            comp = random.choice(leftOverList)
        elif reps2 == "HT" or reps2 == "ht":
            leftOverList = ["HH", "TT"]
            comp = random.choice(leftOverList)
        elif reps2 == "TT" or reps2 == "tt":
            leftOverList = ["HH", "HT"]
            comp = random.choice(leftOverList)
        else:
            print("I didn't understand your answer. Please try again!")
            coinFlips3(L)
    else:
        print("I didn't understand your answer. Please try again!")
        coinFlips3(L)

    userCoinChoices = [reps1, reps2]
    dhCoinChoices = [comp]
    print()
    print("You have chosen the following two coin combinations: ")
    printList(userCoinChoices)
    print("Decision Helper has chosen: ")
    printList(dhCoinChoices)
    print()

    matrixComboToChoices = []
    print("Now choose which coin combination represents which choice") #if i have time: . If you would like Decision Helper to choose, type \'random\' otherwise hit enter")
    printListWithIndex(L)
    rep = ""
    reps = []
    # if input() == "random":
    #     print("do something with random")
    # else:
    for x in userCoinChoices:
        print("What does ", x, " represent? 0, 1, or 2")
        r = input()
        
        
        try:
            r = int(r)   # make into an int!
        except:
            print("I didn't understand your input! Continuting...")
            continue

        if r == 0:
            rep = L[0]
        elif r == 1:
            rep = L[1]
        elif r == 2:
            rep = L[2]
        else:
            print("I didn't understand your input! Continuing...")
            continue
        matrixComboToChoices.append([x,rep])
        print()
        reps.append(rep)
        # printList(matrixComboToChoices)

    #adding the last choice with decision helpers choice
    if reps[0] == L[0]:
        if reps[1] == L[1]: # i know it's not clean, but my brain isn't working and so at least this does
            matrixComboToChoices.append([dhCoinChoices[0],L[2]])
        elif reps[1] == L[2]:
            matrixComboToChoices.append([dhCoinChoices[0],L[1]])
    elif reps[0] == L[1]:
        if reps[1] == L[0]: # i know it's not clean, but my brain isn't working and so at least this does
            matrixComboToChoices.append([dhCoinChoices[0],L[2]])
        elif reps[1] == L[2]:
            matrixComboToChoices.append([dhCoinChoices[0],L[0]])
    elif reps[0] == L[2]:
        if reps[1] == L[0]: # i know it's not clean, but my brain isn't working and so at least this does
            matrixComboToChoices.append([dhCoinChoices[0],L[1]])
        elif reps[1] == L[1]:
            matrixComboToChoices.append([dhCoinChoices[0],L[0]])

    else:
        matrixComboToChoices.append([dhCoinChoices,"marie fails"])

    


    print("The coinflip choices and their representations look like this: ")
    printList(matrixComboToChoices)
    print()
    print("Now the Decision Helper is going to flip the coin twice. The combination that matches the coin flips, means that choice wins.")

    coinFlipOptions = ["H", "T"]
    coinFlip1 = random.choice(coinFlipOptions)
    coinFlip2 = random.choice(coinFlipOptions)
    dhCoinFlips = [coinFlip1, coinFlip2]

    print()
    # print("The coin flips results were:")
    # printList(dhCoinFlips)

    coinFlipsResult = ''.join(dhCoinFlips)
    print("The coin flips results were: ", coinFlipsResult)
    # print()
    

    for coins in matrixComboToChoices:
        for pairs in coins:
            # print("index:", coins.index(pairs), "value: ", pairs)
            if coins.index(pairs) == 0:
                if pairs == coinFlipsResult:
                    # print("pairs == coinFlipsResults:", pairs, "==", coinFlipsResult)
                    if pairs == dhCoinChoices[0]:
                        # print("pairs == dhCoinChoices:", pairs, "==", dhCoinChoices[0])
                        print("Decision Helper wins!")
                        print()
                        return coins[1]
                    elif pairs == userCoinChoices[0] or pairs == userCoinChoices[1]: #user choices
                        # print("pairs == userCoinChoices[0]:", pairs, "==", userCoinChoices[0], "or pairs == userCoinChoices[1]", userCoinChoices[1])
                        print("You win!")
                        print()
                        return coins[1]
                    # else:
                    #     print("MARIE FIGURE IT OUTTT")

    print("The coin flips did not match any of the choices. Going to flip coins again and try it again") #wont be called unless the for loop didnt end with a return
    while True:
        coinFlipOptions = ["H", "T"]
        coinFlip1 = random.choice(coinFlipOptions)
        coinFlip2 = random.choice(coinFlipOptions)
        dhCoinFlips = [coinFlip1, coinFlip2]
        print()
        coinFlipsResult = ''.join(dhCoinFlips)
        print("The coin flips results were: ", coinFlipsResult)
        for coins in matrixComboToChoices:
            for pairs in coins:
                # print("index:", coins.index(pairs), "value: ", pairs)
                if coins.index(pairs) == 0 and pairs == coinFlipsResult:
                    # print("pairs == coinFlipsResults:", pairs, "==", coinFlipsResult)
                    if pairs == dhCoinChoices:
                        # print("pairs == dhCoinChoices:", pairs, "==", dhCoinChoices)
                        print("Decision Helper wins!")
                        print()
                        return coins[1]
                    elif pairs == userCoinChoices[0] or pairs == userCoinChoices[1]: #user choices
                        # print("pairs == userCoinChoices[0]:", pairs, "==", userCoinChoices[0], "or pairs == userCoinChoices[1]", userCoinChoices[1])
                        print("You win!")
                        print()
                        return coins[1]

                    else:
                        print("AHH MARIE FAILEDDDD")
                        break
                else:
                    continue #run again


    # print("This means that ", coinFlipsResult, " won")

def shuffle(L):
    """ takes a list and shuffles them. then asks the uer to choose which index is the right choice. similar to pick a card in a shuffle desk
        leverages random.shuffle function
        input L: list of choices
    """
    print()
    print("Shuffling...")
    print()
    random.shuffle(L)
    print("Please choose what index you would like the decision helper to choose from between 0 and ", len(L)-1, "or choose 'random' and Decision Helper will choose for you")
    indexChoice = input()
    if indexChoice == "random" or indexChoice == "Random" or indexChoice == "RANDOM":
        listIndexs = []

        for x in L:
            indexNumber = L.index(x)
            listIndexs.append(indexNumber)
            # print("listIndexs:", listIndexs)

        # print("listIndexs:", listIndexs)
        x = random.choice(listIndexs)
        print()
        print("Decision Helper randomly chose index: ", x)
        print("After shuffling, the list looked like this: ")
        printListWithIndex(L)
        return L[x]
    else:
        indexChoice = int(indexChoice)
        print()
        print("You chose whatever option lays in index: ", indexChoice)
        print("After shuffling, the list looked like this: ")
        printListWithIndex(L)
        return L[indexChoice]



def Start():
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
                print("You chose option 1) 'Flip a Coin' and the Decision Helper decided: ")
                print("\"", decision, "\"")
                print("Hope that helped!")

            elif kd == 2:
                print()
                print("You chose option 2) Rock, Paper, Scissors")
                decisionRPS = rockPaperScissors2(choices)
                print("And therefore, the decision is: \"", decisionRPS, "\"")
                print()
                while True:
                    print("Would you like to play Rock, Paper, Scissors again with the same choices? Y or N") #play rock paper scissors again with same choices
                    rpsAgain = input()
                    print()
                    if rpsAgain == 'Y' or rpsAgain == 'y' or rpsAgain == 'Yes':
                        print("Here we go again!")
                        decisionRPS = rockPaperScissors2(choices)
                        print("And therefore, the decision is: \"", decisionRPS, "\"")
                        print()
                        continue
                    elif rpsAgain == 'N' or rpsAgain == 'n' or rpsAgain == 'No' or rpsAgain == 'no':
                        print("Ok no problem!")
                        break
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
                        continue
                    elif rpslsAgain == 'N' or rpslsAgain == 'n' or rpslsAgain == 'No' or rpslsAgain == 'no':
                        print("Ok no problem!")
                        break
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
                    print("Would you like to play 4) Random among random again with the same choices? Y or N") #play rock paper scissors again with same choices
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
            kindOfDecisionsThreeChoices()
            kd = input()
            try:
                kd = int(kd)   # make into an int!
            except:
                print("I didn't understand your input...Please Try again!")
                kindOfDecisionsThreeChoices()

            if kd == 1: #choose randomly between the 3
                
                decision = random.choice(choices)
                print()
                print("You chose option 1) 'Random' and the Decision Helper decided: ")
                print("\"", decision, "\"")

                # print("need to test loop still")
                while True: #keep asking until they say no
                    print("Would you like to play 1) Random again with the same choices? Y or N") #play rock paper scissors again with same choices
                    rand3again = input()
                    print()
                    if rand3again == 'Y' or rand3again == 'y' or rand3again == 'Yes' or rand3again == 'yes':
                        print("Here we go again!")
                        decision = random.choice(choices)
                        print("And therefore, the decision is: \"", decision, "\"")
                        print()
                        continue
                    elif rand3again == 'N' or rand3again == 'n' or rand3again == 'No' or rand3again == 'no':
                        print("Ok no problem!")
                        break
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 
                
                print("Hope that helped!")

            elif kd ==2:
                print()
                print("You chose option 2) Coin Flips. This means you'll play a round of coin flips that is meant for 3 choices.")
                coins3decision = coinFlips3(choices)
                print("And therefore, the decision is: \"", coins3decision, "\"")
                print()

                # print("need to test loop still")
                while True: #keep asking until they say no
                    print("Would you like to play 2) Coin Flips again with the same choices? Y or N") #play rock paper scissors again with same choices
                    coins3again = input()
                    print()
                    if coins3again == 'Y' or coins3again == 'y' or coins3again == 'Yes' or coins3again == 'yes':
                        print("Here we go again!")
                        coins3decision = coinFlips3(choices)
                        print("And therefore, the decision is: \"", coins3decision, "\"")
                        print()
                        continue
                    elif coins3again == 'N' or coins3again == 'n' or coins3again == 'No' or coins3again == 'no':
                        print("Ok no problem!")
                        break
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 

            elif kd == 3:
                print()
                print("You chose option 3) Shuffle among choices. This means Decision Helper will shuffle through your" +  
                " and then you'll decide which index to randomly pick.")
                shuffle3Decision = shuffle(choices)
                print()
                print("And therefore, the decision is: \"", shuffle3Decision, "\"")
                
                while True: #keep asking until they say no
                    print()
                    print("Would you like to play 3) Shuffle among choices again with the same choices? Y or N") #play rock paper scissors again with same choices
                    shuffle3again = input()
                    print()
                    if shuffle3again == 'Y' or shuffle3again == 'y' or shuffle3again == 'Yes' or shuffle3again == 'yes':
                        print("Here we go again!")
                        shuffle3Decision = shuffle(choices)
                        print("And therefore, the decision is: \"", shuffle3Decision, "\"")
                        print()
                        continue
                    elif shuffle3again == 'N' or shuffle3again == 'n' or shuffle3again == 'No' or shuffle3again == 'no':
                        print("Ok no problem!")
                        break
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 

            elif kd == 4:
                print()
                print("You chose option 4) 'Random among random'. This means that Decision Helper will create a list of a random multiple (between 0 and 100) " + 
                "of each choice and then choose among said list of choices.") 
                random3decision = randomAmongRandom(choices)
                print()
                print("Decision Helper decided: ")
                print("\"", random3decision, "\"")
                while True: #keep asking until they say no
                    print()
                    print("Would you like to play 4) Random among random again with the same choices? Y or N") #play rock paper scissors again with same choices
                    randOfRand3Again = input()
                    print()
                    if randOfRand3Again == 'Y' or randOfRand3Again == 'y' or randOfRand3Again == 'Yes' or randOfRand3Again == 'yes':
                        print("Here we go again!")
                        random3decision = randomAmongRandom(choices)
                        print("And therefore, the decision is: \"", random3decision, "\"")
                        print()
                        continue
                    elif randOfRand3Again == 'N' or randOfRand3Again == 'n' or randOfRand3Again == 'No' or randOfRand3Again == 'no':
                        print("Ok no problem!")
                        break
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 
                
                print("Hope that helped!")

            
            elif kd ==9:
                break

        elif numChoice == 3:
            print()
            print("You've chosen option 3) More Than Three Choices") 
            print("Please enter your choices. When you're done, type \"done\" as your last choice.")
            choices = []
            while True:
                choice = input()
                # print("choice: ", choice)
                if choice == "done" or choice == "DONE" or choice == "Done":
                    # print("but why")
                    break
                else:
                    # print("but why again?")
                    choices.append(choice)
                    continue

            print()
            print("Great! Your choices were: ")
            printList(choices)
            print()
            print("Now that you've entered your choices...")
            kindOfDecisionMoreThanThreeChoices()
            kd = input()
            try:
                kd = int(kd)   # make into an int!
            except:
                print("I didn't understand your input...Please Try again!")
                kindOfDecisionMoreThanThreeChoices()

            if kd == 1: #choose randomly between the 3
                
                rand3plusagain = random.choice(choices)
                print()
                print("You chose option 1) 'Random' and the Decision Helper decided: ")
                print("\"", rand3plusagain, "\"")

                # print("need to test loop still")
                while True: #keep asking until they say no
                    print("Would you like to play 1) Random again with the same choices? Y or N") #play rock paper scissors again with same choices
                    rand3again = input()
                    print()
                    if rand3plusagain == 'Y' or rand3plusagain == 'y' or rand3plusagain == 'Yes' or rand3plusagain == 'yes':
                        print("Here we go again!")
                        rand3plusagain = random.choice(choices)
                        print("And therefore, the decision is: \"", rand3plusagain, "\"")
                        print()
                        continue
                    elif rand3plusagain == 'N' or rand3plusagain == 'n' or rand3plusagain == 'No' or rand3plusagain == 'no':
                        print("Ok no problem!")
                        break
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 
            if kd == 2:
                print()
                print("You chose option 2) Shuffle among choices. This means Decision Helper will shuffle through your" +  
                " and then you'll decide which index to randomly pick.")
                shuffle3PlusDecision = shuffle(choices)
                print()
                print("And therefore, the decision is: \"", shuffle3PlusDecision, "\"")
                
                while True: #keep asking until they say no
                    print()
                    print("Would you like to play 2) Shuffle among choices again with the same choices? Y or N") #play rock paper scissors again with same choices
                    shuffle3plusagain = input()
                    print()
                    if shuffle3plusagain == 'Y' or shuffle3plusagain == 'y' or shuffle3plusagain == 'Yes' or shuffle3plusagain == 'yes':
                        print("Here we go again!")
                        shuffle3PlusDecision = shuffle(choices)
                        print("And therefore, the decision is: \"", shuffle3PlusDecision, "\"")
                        print()
                        continue
                    elif shuffle3plusagain == 'N' or shuffle3plusagain == 'n' or shuffle3plusagain == 'No' or shuffle3plusagain == 'no':
                        print("Ok no problem!")
                        break
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 

            elif kd == 3:
                print()
                print("You chose option 3) 'Random among random'. This means that Decision Helper will create a list of a random multiple (between 0 and 1000) " + 
                "of each choice and then choose among said list of choices.") 
                rand3plusdecision = randomAmongRandom(choices)
                print("Decision Helper decided: ")
                print("\"", rand3plusdecision, "\"")
                while True: #keep asking until they say no
                    print("Would you like to play 4) Random among random again with the same choices? Y or N") #play rock paper scissors again with same choices
                    randOfRand3PlusAgain = input()
                    print()
                    if randOfRand3PlusAgain == 'Y' or randOfRand3PlusAgain == 'y' or randOfRand3PlusAgain == 'Yes' or randOfRand3PlusAgain == 'yes':
                        print("Here we go again!")
                        rand3plusdecision = randomAmongRandom(choices)
                        print("And therefore, the decision is: \"", rand3plusdecision, "\"")
                        print()
                        continue
                    elif randOfRand3PlusAgain == 'N' or randOfRand3PlusAgain == 'n' or randOfRand3PlusAgain == 'No' or randOfRand3PlusAgain == 'no':
                        print("Ok no problem!")
                        break
                    else:
                        print("I didn't understand your input! Continuting...")
                        continue 
                
                print("Hope that helped!")


        
        
        elif numChoice == 9:
            break
            
        else:
            print("I didn't understand your answer. Please try again!")
            Start()


        print()
        print("Are you done deciding? Y or N")
        doneAns = input()
        if doneAns == 'N' or doneAns == 'n' or doneAns == 'no':
            print("\nOk, another round it is!")
            continue
        else:
            print("\nCongrats! Have a good one :)")
            break


# DEMOS ARE AWESOME!!!

""" functions used from random library:
    random.choice()
    random.randrange()


"""




"""
#things to use:

random.randint(a, b)
    Return a random integer N such that a <= N <= b.
    option for randomly choosing which type of decisionhelper function
    ?even for which number of decisions


√random.shuffle(x[, random])¶
    Shuffle the sequence x in place. The optional argument random is a 0-argument function returning a random float in [0.0, 1.0); by default, this is the function random().
    Note that for even rather small len(x), the total number of permutations of x is larger than the period of most random number generators; this implies that most permutations of a long sequence can never be generated.

    use for multiple choices - shuffle and choose the one in L[0]


random.random()
    Return the next random floating point number in the range [0.0, 1.0).
    use for random of random


"""