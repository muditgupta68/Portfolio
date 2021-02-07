# module for hangman
# logics down below
import random
def hangmanMethod(player):
    movieLst = ['baaghi3','thankyou','welcome','my name is khan','dhoom','angrezi medium','race','dangal','dabangg','boss','housefull 1','housefull 2','housefull 3','don 2','don','hera pheri','pk','raabta','rab ne banadi jodi','om shanti om','agneepath','fanaa','ms dhoni','sanju','raees','munna bhai','panga']
    movie = random.choice(movieLst)
    lives = 15
    rndmMovielst = list(movie)
    guessedLetter = []
    guessinglst = []
    for i in rndmMovielst:
        guessinglst.append('_')
    print('\t⬤ Guess the Movie :-')
    print('\t',guessinglst)
    print('\n')
    flag = 0
    pointsEarned = 0

    while lives > 0 and flag == 0:
        guess = input('\t➽ Guess the character\t')
        guessLen = len(guess)
        if guess in guessedLetter:
            print('\n\t☼ You already used the character, try something else\n')

        elif guessLen > 1:
            print('\n\t☼ You entered more than a character! Try again by entering one letter!!\n')

        else:
            guessedLetter.append(guess)
            lenMovie = len(rndmMovielst)
            if guess in rndmMovielst:
                for i in range(0,lenMovie,1):
                    if guess == rndmMovielst[i]:
                        print('\n\t☀ great! correct character guessed ✔')
                        locIndex = i
                        guessinglst[locIndex] = guess
                        print('\t',guessinglst,'\n')
            else:
                    print("\n\t☼ oof! Wrong character ✘! Try again ☠")
                    lives = lives - 1
                    print('\t➣',lives," lives left!")
                    print('\t', guessinglst, '\n')

        if guessinglst == rndmMovielst:
            dataFile = open('gamehistory.txt','a')
            print('\n\t▶ You won! Congratulations!! 😃♛')
            pointsEarned = (lives * 10)
            print('\t▶ Points earned : \t',pointsEarned,' /150')
            dataFile.write(player)
            dataFile.write('\twon! Congratulations!!')
            dataFile.write('\tPoints earned:')
            strPoint = str(pointsEarned)
            dataFile.write(strPoint)
            dataFile.write('\n')
            dataFile.close()
            flag = 1

        elif lives == 0:
            dataFile = open('gamehistory.txt', 'a')
            print('\n\t☼ OOFF! You lost! Better luck next time ⚠️')
            print('The movie was: ', rndmMovielst)
            pointsEarned = (lives * 10)
            print('\t▶ Points earned : \t', pointsEarned, ' /150')
            dataFile.write(player)
            dataFile.write('\tOOFF! You lost! Better luck next time')
            dataFile.write('\tPoints earned:')
            strPoint = str(pointsEarned)
            dataFile.write(strPoint)
            dataFile.write('\n')
            dataFile.close()
        else:
            pass

