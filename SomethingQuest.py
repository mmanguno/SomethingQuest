# Mitchell Manguno
# mmanguno3@gatech.edu
# I worked on the homework assignment alone, using this semester's course materials, in addition
# to:
# 1. stackoverflow.com/questions/11552320/correct-way-to-pause-python-program, for the sleep function
# 2. stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python, for clearing the screen
# 3. stackoverflow.com/questions/73663/terminating-a-python-script, for the exit function

from time import sleep #This delays functions by a prescribed amount of time
from os import system #This was used to clear the screen, rather than have it cluttered
from random import randint #Yields a psuedo-random integer
from sys import exit #This kills the program

class char():
    """This class is used to make characters with explicitly given and derived statistics"""
    def __init__(self, className, name, strength, endurance, intelligence, sneak):
        self.className = className
        self.name = name
        self.strength = strength
        self.endurance = endurance
        self.sneak = sneak
        self.intelligence = intelligence
        self.health = (15 + (2*endurance) + strength) #These last two statistics are derived from the explicit stats above, and are calculated independent of the user's input
        self.magicka = ((2*intelligence) + 5)

def sizzler():
    """This is the 'sizzler' text, a kind of plot intro. Is not used in the completed game."""
    print("--------------------------------------------------------------------------------------")
    sleep(3)
    print("            Long in the many futures, when the cities of gray tumble and fall...")
    sleep(5)    #Delays the printing of the next line by 5 seconds.
    print("        The present-ancients awoke the slumbering force dwelt within the world...")
    sleep(5)
    print("        The eldritch magicks rose up to reform the world to that of the imagination...")
    sleep(5)
    print("        The world was rent and ripped from reality, and was turned into what every")
    print("        amateur fantasy writer dreams of...")
    sleep(5)
    print(" ")
    print("        This is the world of...")
    sleep(2)
    print(" ")
    print("                           SOMETHING QUEST!")
    print(" ")
    sleep(3)


#Here's your run-of-the-mill main menu
def mainMenu():
    """A main menu where the user may start the game, read the credits, or quit."""
    what = 0
    while what == 0:
        system('cls') #Clears the screen in Windows (non-Unix based systems)
        system('clear') #Clears the screen in linux and Mac OS (Unix based systems)
        print("                ###########################################")
        print("                # \          \ *************** /        / #")
        print("                #  \---------- SOMETHING QUEST ------- /  #")
        print("                #  /         / *************** \       \  #")
        print("                ###########################################")
        print("                                                           ")
        print("                   A shambling skeleton of a textual RPG   ")
        print("                -------------------------------------------")
        print("                                                           ")
        print(" ")
        print("1. Start Game")
        print("2. Random Battle Arena")
        print("3. About")
        print("4. Quit")
        menuChoice = input("?   ")
        if menuChoice == "1": #Starts the main plot
            what = 1
            SomethingQuest()
        elif menuChoice == "2": #An 'arena' wherein the user makes a character and battles against a random enemy of random level
            what = 1
            playerCharacter = charCreation()
            randomBattleIndex = 1
            while randomBattleIndex != 0:
                enemyLvl = randint(0, 10)
                randomBattle(enemyLvl)
                system('cls')
                system('clear')
                print("        Again?")
                rbc = input("[Y/N]   ")
                if rbc == "N" or rbc == "n" or rbc == "no" or rbc == "No":
                    randomBattleIndex = 0
            mainMenu()
        elif menuChoice == "3": #About
            what = 1
            system('cls')
            system('clear')
            print("Version: 1.01")
            print("Made by Mitchell Manguno, 2013, for Dr. Jay Summet's CS 1301")
            print("Written in Python 3.3.2+ in Ubuntu Linux, in Vim")
            print(" ")
            itdoesntmatterwhatthisiscalled = input("Press Return or Enter when done")
            mainMenu()
        elif menuChoice =="4": #Kills the program
            system('cls')
            system('clear')
            exit() #This kills the program.  It is better to use this than 'return', as, if I'm deep within a chain of functions, I want this to kill the whole thing rather than return None up a level
        elif menuChoice != "4" and menuChoice != "3" and menuChoice != "2" and menuChoice != "1":
            print(" ")
            print("Invalid Input. Try Again.")
            sleep(2)
def charCreation():
    """Makes the player-character using the char class and some simple conditionals."""
    churroDecision = 1
    while churroDecision == 1:
        global playerCharacter 
        system('cls')
        system('clear')
        name = input("What is the name of your character?   ") #Gives a name to the playerCharacter
        print(" ")
        print("What class will you choose?")
        print(" ")
        print("---------------------------------------------------------------------")
        print("            #1              #2            #3                 #4      ")
        print("          Warrior          Mage          Rogue         Make Your Own ")
        print("         ---------        ------        -------       ---------------")
        print("Stength:    10              03            05                 ??      ")
        print("Endurance:  08              05            06                 ??      ")
        print("Intellig.:  01              12            03                 ??      ")
        print("Sneak:      06              05            11                 ??      ")
        print("---------------------------------------------------------------------")
        print(" ")
        classChoice = input("Choice:   ") #Allows choice between the 3 pre-determined classes or for the user to make their own.
        if classChoice == "1" or classChoice == "#1":
            playerCharacter = char("Warrior", name, 10, 8, 1, 6)
        elif classChoice == "2" or classChoice == "#2":
            playerCharacter = char("Mage", name, 3, 5, 12, 5)
        elif classChoice == "3" or classChoice == "#3":
            playerCharacter = char("Rogue", name, 5, 6, 3, 11)
        elif classChoice == "4" or classChoice == "#4":
            print("-------------")
            print("The class stats must be, combined, less-than-or-equal-to 25")
            print("No values may be negative")
            print("-------------")
            MYOClass = input("Class Name:   ")
            negativeCheck = 0
            x = 0
            while x != 1:
                negativeCheck = 0
                try:
                    MYOStrength  = int(input("Class Strength:   "))
                    if MYOStrength < 0:
                        print("NO NEGATIVE VALUES")
                        print("Now you're going to have to do this all over again")
                        negativeCheck = 1
                    MYOEndurance = int(input("Class Endurance:   "))
                    if MYOEndurance < 0:
                        print("NO NEGATIVE VALUES")
                        print("Now you're going to have to do this all over again")
                        negativeCheck = 1
                    MYOIntellig = int(input("Class Intellig.:   "))
                    if MYOIntellig < 0:
                        print("NO NEGATIVE VALUES")
                        print("Now you're going to have to do this all over again")
                        negativeCheck = 1
                    MYOSneak  = int(input("Class Sneak:   "))
                    if MYOSneak < 0:
                        print("NO NEGATIVE VALUES")
                        print("Now you're going to have to do this all over again")
                        negativeCheck = 1
                    if ( MYOStrength + MYOEndurance + MYOIntellig + MYOSneak) > 25 or negativeCheck == 1: #Makes sure that the user does not make a class with stats that add up to greater than 25
                        print(" ")
                        print("Something went wrong. You did something wrong.")
                        print("-------------")
                    else:
                        playerCharacter = char(MYOClass, name, MYOStrength, MYOEndurance, MYOIntellig, MYOSneak) #Creates the custom class
                        x = 1 #Breaks the loop
                except ValueError:
                    print(" ")
                    print("Why do you do this?")
                    sleep(3)
                    print("Try again.")
                    sleep(2)
                    x = 0
        else:
            print(" ")
            print("        WRONG")
            sleep(3)
        print("You have chosen...") #Prints out the custom class
        print("        A", playerCharacter.className, "by the name of", playerCharacter.name)
        print("He/She has...")
        print("        ", playerCharacter.strength, "points of Strength")
        print("        ", playerCharacter.endurance, "points of Endurance")
        print("        ", playerCharacter.intelligence, "points of Intelligence")
        print("        ", playerCharacter.sneak, "points of Sneak")
        print("        ", playerCharacter.health, "hit-points, and")
        print("        ", playerCharacter.magicka, "points of magicka")
        print(" ")
        charDecision = input("Is this correct? [Y/N]   ")
        if charDecision == "Y" or charDecision == "y" or charDecision == "yes" or charDecision == "Yes":
            return playerCharacter  #Returns the playerCharacter, finishing charCreation
        if charDecision == "N" or charDecision == "n" or charDecision == "no" or charDecision == "No":
            pass #If the user is unhappy with their decision, charCreate() again
        else:
            print("        I don't know what you did.  I just don't know.")
            sleep(3)
            print("        Let's try this again.")
            sleep(3)

#---Ye Olde Dictionary of Enemies---#
enemyLevel = 0 #Allows the enemies to be scaled by a manually inputted 'level'
ENEMIES = { "Grue":char("Grue", "Grue", 3+enemyLevel, 3+enemyLevel, 1+enemyLevel, 0), "Wolf":char("Wolf", "Wolf", 5+enemyLevel, 6+enemyLevel, 2+enemyLevel, 3+enemyLevel), "Black Knight":char("Black Knight", "Black Knight", 8+enemyLevel, 6+enemyLevel, 5+enemyLevel, 1+enemyLevel), "Battlemage":char("Battlemage", "Battlemage", 7+enemyLevel, 6+enemyLevel, 7+enemyLevel, 2+enemyLevel) } #A dictionary full of the whole list of enemies
enemyNumeric = { 1: "Grue", 2:"Wolf", 3:"Black Knight", 4:"Battlemage" } #Used for the 'randomBattle' function to choose the enemy
#-----------------------------------#

def randomBattle(enemyLvl):
    """Randomly picks an enemy of a prescribed level to fight the playerCharacter."""
    global playerCharacter #Imports the playerCharacter and its stats
    enemyLevel = enemyLvl #Assigns the enemy's level
    choosingVariable = randint(1,4) #Gets a pseudo-random variable used to choose the enemy
    enemy = ENEMIES[enemyNumeric[choosingVariable]] 
    system('cls')
    system('clear')
    battleIndex = 1 #Primes an index for a while loop 
    enemyHealth = enemy.health * 1 #Makes a clone of enemy.health; we don't want the actual attribute to be changed every time a battle occurs: that would disturb the system and its independent calculations
    playerHealth = playerCharacter.health * 1 #Makes a clone of playerCharacter.health; see above for rationale
    playerMagicka = playerCharacter.magicka * 1 #Makes a clone of playerCharacter.magicka; see above for rationale
    while battleIndex == 1: #Initiates the while loop
        system('cls')
        system('clear')
        enemySpaces = 26 - len(enemy.name) - len(str(enemyLvl))
        enemyHitPointsSpaces = 21 - len(str(enemyHealth))
        nameSpaces = 51 - len(playerCharacter.name)
        hPSpaces = 45 - len(str(playerHealth))
        magickaSpaces = 48 - len(str(playerMagicka))
        print("        ############################################################")
        print("        #                         Level "+str(enemyLvl)+" "+enemy.name+ " "*enemySpaces+"#")
        print("        #                         Hit-Points: "+str(enemyHealth)+ " "*enemyHitPointsSpaces+"#")
        print("        #                                                          #")
        print("        # Name: "+playerCharacter.name+" "*nameSpaces+"#")
        print("        # Hit-Points: "+str(playerHealth)+" "*hPSpaces+"#")
        print("        # Magicka: "+str(playerMagicka)+" "*magickaSpaces+"#")
        print("        ############################################################")
        print(" ")
        print("1. Physical Attack")
        print("2. Magickal Attack")
        if playerCharacter.intelligence >= 7: #If playerCharacter is intelligent enough...
            print("H. Health Spell") #Allow the use of a healing spell
        print(" ")
        battleChoice = input("?   ") #Player turn
        playerVariation = randint(0,2) #Gives the player attack some slight variation; makes it more realistic
        enemyVariation = randint(0,2) #Gives the enemy attack some slight variation; makes it more...realistic?
        if battleChoice =="1": #If Physical attack...
            enemyHealth = enemyHealth - (playerCharacter.strength + playerVariation) #Reduce enemyHealth by playerCharacter.strength + variation
            print("You did "+str(playerCharacter.strength+playerVariation)+" physical damage to the enemy "+enemy.name+".") #Prints the action
            sleep(1)
        elif battleChoice =="2" and playerMagicka >= playerCharacter.intelligence: #If Magickal attack...
            enemyHealth = enemyHealth - (playerCharacter.intelligence + playerVariation) #Reduce enemyHealth by playerCharacter.intelligence + variation
            playerMagicka = playerMagicka - (playerCharacter.intelligence + playerVariation) #Reduce playerMagicka by playerCharacter.intelligence + variation, the spell's cost
            print("You did "+str(playerCharacter.intelligence + playerVariation)+" magickal damage to the enemy "+enemy.name+".")
            sleep(1)
        elif battleChoice == "2" and playerMagicka < playerCharacter.intelligence: #If Magickal attack but no magicka...
            print("You don't have enough magicka. You lose a turn fumbling")
            print("about.") #Lose a turn.
            sleep(2)
        elif battleChoice == "H" and (playerMagicka >= playerCharacter.intelligence + playerVariation): #If heal...
            print("You heal for "+str(playerCharacter.intelligence + playerVariation)+" hit-points")
            playerHealth = playerHealth + (playerCharacter.intelligence + playerVariation) #Add playerCharacter.intelligence + variation to playerHealth
            playerMagicka = playerMagicka - (playerCharacter.intelligence + playerVariation) #Reduce playerMagicka by playerCharacter.intelligence + variation
        elif battleChoice == "H" and playerMagicka < (playerCharacter.intelligence + playerVariation): #If heal but no magicka...
            print("You don't have enough magicka. You lose a turn fumbling")
            print("about.") #Lose a turn
            sleep(2)
        elif battleChoice == "h" and playerMagicka >= (playerCharacter.intelligence + playerVariation): #If heal...
            print("You heal for "+str(playerCharacter.intelligence + playerVariation)+" hit-points")
            playerHealth = playerHealth + (playerCharacter.intelligence + playerVariation) #Add playerCharacter.intelligence + variation to playerHealth
            playerMagicka = playerMagicka - (playerCharacter.intelligence + playerVariation) #Reduce playerMagicka by playerCharacter.intelligence + variation
        elif battleChoice == "h" and playerMagicka < (playerCharacter.intelligence + playerVariation): #If heal but no magicka...
            print("You don't have enough magicka. You lose a turn fumbling")
            print("about.") #Lose a turn
            sleep(2)
        if playerHealth < 1: #If dead...
            print("You somehow managed to kill yourself")
            sleep(3)
            print("Congratulations!  I didn't even know you could do that!")
            sleep(3)
            gameOver() #Die
        if enemyHealth < 1: #If enemy dead...
            print("You killed the enemy "+enemy.name+".") #Enemy die
            sleep(2)
            battleIndex = 0 #End battle sequence
            return None
        enemyBattleChoice = randint(10, 11) #Enemy turn: either magickal attack or physical attack
        if enemyBattleChoice == 11: #Attacks playerCharacter by enemy.strength + variation
            print("The  "+enemy.name+" struck you for "+str(enemy.strength+enemyVariation)+" physical damage")
            sleep(1)
            playerHealth = playerHealth - (enemy.strength + enemyVariation)
        elif enemyBattleChoice == 10: #Attacks playerCharacter by enemy.intelligence + variation
            print("The "+enemy.name+" struck you for "+str(enemy.intelligence+enemyVariation)+" magickal damage")
            sleep(1)
            playerHealth = playerHealth - (enemy.intelligence+enemyVariation)
        if playerHealth < 1: #If dead...
            print("The enemy "+enemy.name+" killed you.")
            sleep(2)
            gameOver() #Die
        if enemyHealth < 1: #If enemy dead...
            print("The enemy "+enemy.name+" killed itself.")
            sleep(2)
            print("You are a terrible person.")
            battleIndex = 0 #Enemy Die
            return None

def scriptedBattle(enemyLvl, chosenEnemy): #The comments for this are the same as in randomBattle().  They are the same functions, excepting for two lines
    """Has the playerCharacter fight a chosen enemy with a prescribed level."""
    global playerCharacter
    enemy = ENEMIES[chosenEnemy] #Assigns enemy to the chosen enemy parameter
    enemyLevel = enemyLvl
    system('cls')
    system('clear')
    battleIndex = 1 #Primes an index for a while loop 
    enemyHealth = enemy.health * 1 #Makes a clone of enemy.health; we don't want the actual attribute to be changed every time a battle occurs: that would disturb the system and its independent calculations
    playerHealth = playerCharacter.health * 1 #Makes a clone of playerCharacter.health; see above for rationale
    playerMagicka = playerCharacter.magicka * 1 #Makes a clone of playerCharacter.magicka; see above for rationale
    while battleIndex == 1: #Initiates the while loop
        system('cls')
        system('clear')
        enemySpaces = 26 - len(enemy.name) - len(str(enemyLvl))
        enemyHitPointsSpaces = 21 - len(str(enemyHealth))
        nameSpaces = 51 - len(playerCharacter.name)
        hPSpaces = 45 - len(str(playerHealth))
        magickaSpaces = 48 - len(str(playerMagicka))
        print("        ############################################################")
        print("        #                         Level "+str(enemyLvl)+" "+enemy.name+ " "*enemySpaces+"#")
        print("        #                         Hit-Points: "+str(enemyHealth)+ " "*enemyHitPointsSpaces+"#")
        print("        #                                                          #")
        print("        # Name: "+playerCharacter.name+" "*nameSpaces+"#")
        print("        # Hit-Points: "+str(playerHealth)+" "*hPSpaces+"#")
        print("        # Magicka: "+str(playerMagicka)+" "*magickaSpaces+"#")
        print("        ############################################################")
        print(" ")
        print("1. Physical Attack")
        print("2. Magickal Attack")
        if playerCharacter.intelligence >= 7: #If playerCharacter is intelligent enough...
            print("H. Health Spell") #Allow the use of a healing spell
        print(" ")
        battleChoice = input("?   ") #Player turn
        playerVariation = randint(0,2) #Gives the player attack some slight variation; makes it more realistic
        enemyVariation = randint(0,2) #Gives the enemy attack some slight variation; makes it more...realistic?
        if battleChoice =="1": #If Physical attack...
            enemyHealth = enemyHealth - (playerCharacter.strength + playerVariation) #Reduce enemyHealth by playerCharacter.strength + variation
            print("You did "+str(playerCharacter.strength+playerVariation)+" physical damage to the enemy "+enemy.name+".") #Prints the action
            sleep(1)
        elif battleChoice =="2" and playerMagicka >= playerCharacter.intelligence: #If Magickal attack...
            enemyHealth = enemyHealth - (playerCharacter.intelligence + playerVariation) #Reduce enemyHealth by playerCharacter.intelligence + variation
            playerMagicka = playerMagicka - (playerCharacter.intelligence + playerVariation) #Reduce playerMagicka by playerCharacter.intelligence + variation, the spell's cost
            print("You did "+str(playerCharacter.intelligence + playerVariation)+" magickal damage to the enemy "+enemy.name+".")
            sleep(1)
        elif battleChoice == "2" and playerMagicka < playerCharacter.intelligence: #If Magickal attack but no magicka...
            print("You don't have enough magicka. You lose a turn fumbling")
            print("about.") #Lose a turn.
            sleep(2)
        elif battleChoice == "H" and (playerMagicka >= playerCharacter.intelligence + playerVariation): #If heal...
            print("You heal for "+ str(playerCharacter.intelligence + playerVariation) + " hit-points")
            playerHealth = playerHealth + (playerCharacter.intelligence + playerVariation) #Add playerCharacter.intelligence + variation to playerHealth
            playerMagicka = playerMagicka - (playerCharacter.intelligence + playerVariation) #Reduce playerMagicka by playerCharacter.intelligence + variation
        elif battleChoice == "H" and playerMagicka < (playerCharacter.intelligence + playerVariation): #If heal but no magicka...
            print("You don't have enough magicka. You lose a turn fumbling")
            print("about.") #Lose a turn
            sleep(2)
        elif battleChoice == "h" and playerMagicka >= (playerCharacter.intelligence + playerVariation): #If heal...
            print("You heal for "+str(playerCharacter.intelligence + playerVariation) + " hit-points")
            playerHealth = playerHealth + (playerCharacter.intelligence + playerVariation) #Add playerCharacter.intelligence + variation to playerHealth
            playerMagicka = playerMagicka - (playerCharacter.intelligence + playerVariation) #Reduce playerMagicka by playerCharacter.intelligence + variation
        elif battleChoice == "h" and playerMagicka < (playerCharacter.intelligence + playerVariation): #If heal but no magicka...
            print("You don't have enough magicka. You lose a turn fumbling")
            print("about.") #Lose a turn
            sleep(2)
        if playerHealth < 1: #If dead...
            print("You somehow managed to kill yourself")
            sleep(2)
            print("Congratulations!  I didn't even know you could do that!")
            gameOver() #Die
        if enemyHealth < 1: #If enemy dead...
            print("You killed the enemy "+enemy.name+".") #Enemy die
            sleep(2)
            battleIndex = 0 #End battle sequence
            return None
        enemyBattleChoice = randint(10, 11) #Enemy turn: either magickal attack or physical attack
        if enemyBattleChoice == 11: #Attacks playerCharacter by enemy.strength + variation
            print("The  "+enemy.name+" struck you for "+str(enemy.strength+enemyVariation)+" physical damage")
            sleep(1)
            playerHealth = playerHealth - (enemy.strength + enemyVariation)
        elif enemyBattleChoice == 10: #Attacks playerCharacter by enemy.intelligence + variation
            print("The "+enemy.name+" struck you for "+str(enemy.intelligence+enemyVariation)+" magickal damage")
            sleep(1)
            playerHealth = playerHealth - (enemy.intelligence+enemyVariation)
        if playerHealth < 1: #If dead...
            print("The enemey "+enemy.name+" killed you.")
            sleep(2)
            gameOver() #Die
        if enemyHealth < 1: #If enemy dead...
            print("The enemy "+enemy.name+" killed itself.")
            sleep(2)
            print("You are a terrible person.")
            battleIndex = 0 #Enemy Die
            return None

def gameOver():
    """A function that triggers once the game ends or if the playerCharacter's health reaches 0 or below."""
    system('cls')
    system('clear')
    print("        #############################################")
    print("        #                                           #")
    print("        #                 GAME OVER                 #")
    print("        #                                           #")
    print("        #############################################")
    print(" ")
    playAgain = input("Play Again? [Y/N]   ")
    if playAgain == "Y" or playAgain == "y" or playAgain == "Yes" or playAgain == "yes":
        mainMenu()
    else:
        system('cls') #Clears the screens
        system('clear')
        exit()

def plot():
    """The plot of the game.  It only serves to demonstrate the scripted battle system and some Morton's Fork conditionals."""
    system('cls')
    system('clear')
    print("            You wake up. Everywhere around you is black.")
    sleep(3)
    print("        There is a faint growling sound behind you.")
    sleep(3)
    print("        You stand up, and meet the GRUE behind you.")
    sleep(3)
    print("        Without a choice, you must battle it.")
    sleep(3)
    scriptedBattle(1, "Grue")
    system('cls')
    system('clear')
    print("            With the fell beast now dead, you see a crack of light.")
    sleep(3)
    print("        You follow the light outside, to a gray & green forest.")
    sleep(3) 
    choice1index = 1
    while choice1index != 0:
        print(" ")
        print("         You have two options...")
        print(" ")
        print("    1. Go back inside the cave...")
        print("    2. Search about the forest...")
        print(" ")
        choice1 = input("?   ")
        if choice1 =="1":
            print("        You go back into the cave.  You find nothing of use.")
            sleep(3)
            print("        You go back outside.")
        if choice1 == "2":
            choice1index = 0
        else:
            print("I cannot parse your choice.")
            sleep(3)
            print("Please enter a valid choice.")
    system('cls')
    system('clear')
    print("            You search about the forest for some signs of civilization")
    print("        or for something of use.")
    sleep(3)
    print("            You see a WOLF up ahead. Do you...")
    print(" ")
    print("    1. Engage the beast.")
    print("    2. Attempt to avoid it.")
    choice2 = input("?   ")
    if choice2 == "1":
        print(" ")
        print("            You prepare for battle and engage the WOLF.")
        sleep(3)
        scriptedBattle(3, "Wolf")
    if choice2 == "2" and playerCharacter.sneak >= 7:
        print(" ")
        print("            You deftly escape the senses of the wolf and continue on.")
        sleep(3)
    if choice2 == "2" and playerCharacter.sneak < 7:
        print(" ")
        print("            You attempt some vaguely acrobatic moves in a failed")
        sleep(3)
        print("        attempt at sneaking. The WOLF gives a confused look, and")
        sleep(3)
        print("        proceeds to attack.")
        sleep(3)
        scriptedBattle(4, "Wolf")
    else:
        print("            "+choice2+"? What is that? You know what, you fight the WOLF.")
        sleep(3)
        print("        The WOLF gains 3 levels.")
        sleep(3)
        scriptedBattle(6, "Wolf")
    system('cls')
    system('clear')
    print("            After slaying the WOLF, you see a glimmering light beyond the")
    sleep(3)
    print("        horizon.  It appears to be a town.  You go towards it.")
    sleep(3)
    system('cls')
    system('clear')
    print("            The town walls bear the sign 'Kyern'.  The town appears to be")
    sleep(3)
    print("        quite small in size. As you move through the village, the air")
    sleep(3)
    print("        around you becomes hazy.  Nausea comes over you, and a faint thougt")
    sleep(3)
    print("        pops into your head. It says...")
    sleep(3)
    print(" ")
    print("                                     DEMO OVER")
    print(" ")
    print("                                Thanks for playing.")
    sleep(5)


playerCharacter = 0 #Declares playerCharacter so the global calls (which allow the same 'playerCharacter' variable to work in multiple functions) will work, as it cannot import an undeclared variable

def SomethingQuest():
    """Holds the entire game together."""
    system('cls')
    system('clear')
    #sizzler()
    global playerCharacter
    playerCharacter = charCreation() #charCreation returns playerCharacter
    plot()
    mainMenu()
    
mainMenu()
