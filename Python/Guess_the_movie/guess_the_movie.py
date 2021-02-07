# ------------------------------------------------GUESS THE MOVIE--------------------------------------------------------------
import hngmnModule
import time

class game:
    def introDet(self):

        self.fstName = input("\t\tEnter your first name: \t\t\t\t\t\t")
        choice = input("\t\t(Do you have Middle Name?(Y/N))\t\t\t\t")
        if choice == 'Y' or choice == 'y' or choice == 'yes' or choice == 'Yes' or choice == 'YES':
            self.midName = input("\t\tEnter your middle name: \t\t\t\t\t")
        else:
            self.midName = ''
        self.lstName = input("\t\tEnter your last name: \t\t\t\t\t\t")
        self.plyrAge = int(input('\t\tEnter your age: \t\t\t\t\t\t\t'))
        decName = input('\t\tDo you want to use your first name as your game name?(Y/N)\t')
        if decName == 'Y' or decName == 'y' or decName == 'yes' or decName == 'Yes' or decName == 'YES':
            self.plyrName = self.fstName
        else:
            self.plyrName = input('\t\tEnter your Name for the game:\t\t\t\t')

    def dispInfo(self):
        print('\n\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('\t\t\tDETAILS')
        print('♜\t NAME: \t\t\t\t',self.fstName + ' ' + self.midName + ' ' + self.lstName)
        print('♜\t AGE: \t\t\t\t',self.plyrAge)
        print('♜\t PLAYER NAME: \t\t', self.plyrName)
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    def begin(self):
        print('\n\n')
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("₪\tWELCOME TO THE GAME ", self.plyrName)
        print("\tAre you ready for the challenge ;)?")
        choice = input('\t\tyes/no\t\t')
        if choice == 'NO' or choice == 'no' or choice == 'No':
            exit()
        else:
            print('\n➣\tLets begin with the Rules at First:-')
            print('\t❶ Random movie name will be taken by NPC and you have to guess the name of the movie.')
            print('\t❷ In each round, you have to enter characters which includes "small letter","numbers" and even "spaces".')
            print('\t❸ You will be given 15 chances or lives to guess the characters.')
            print('\t\t\t\t BEST OF LUCK!\n\n')
            print('------------------------------------------------------------------------------------GAME BEGINS------------------------------------------------------------------------------------------------------')
            print('\n')

    def inPlayrName(self):
        return  self.plyrName


# user-display screen
g1 = game()
print('--------------------------------------------------------------------------------------------------WELCOME--------------------------------------------------------------------------------------------------------')

print("\n➣\tEnter the details below:-")
g1.introDet()
g1.dispInfo()
confDet = input('\n\n\tDo you wish to alter your details (Y/N) ?\t\t')
if confDet == 'Y' or confDet == 'y' or confDet == 'yes' or confDet == 'Yes' or confDet == 'YES':
    g1.introDet()
else:
    pass
g1.begin()
time.sleep(10)
player = g1.inPlayrName()
hngmnModule.hangmanMethod(player)
playAgain = input("\n\t ◖Do you want to play again?◗\t")
while playAgain == 'y' or playAgain == 'yes' or playAgain == 'Yes' or playAgain == 'YES':
    print('\n')
    hngmnModule.hangmanMethod(player)
    playAgain = input("\n\t ◖Do you want to play again?◗\t")

if playAgain == 'n' or playAgain == 'no' or playAgain == 'No' or playAgain == 'NO':
    print('\n\n')
    print('⫷ THANKYOU FOR PLAYING ⫸ ')
    print('⫷ HOPE TO SEE YOU AGAIN ⫸ ')
    exit()

# ------------------------------------------------------------END-------------------------------------------------------

