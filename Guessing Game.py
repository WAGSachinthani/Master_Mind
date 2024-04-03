
#Importing randoms
import random


#play again or not
round = 0
while True:
    round += 1

    if round== 2:
        print("you have scored ",score,"points")
        again = input("Do you want to play another game (Yes/No) ?")
        if again == "yes":
            round=0
            continue
        else:
            exit()
            
            


#get user inputs
    my_name=input("Enter your name here: ")




#display users name 
    print("    "," "," ","","","","","","","","","","","","","HI,",my_name,"WELCOME TO THE GAME!")

#giving instructions

    print("You have only  8 attempts.")


#display color code
    print("Number to guess-XXXX""  ","    ","  ","  ","  ","","","","","","","","","","","Color mapping:")
    print("","","","","","","","","","","","","","","","","","","","","","","","","","","","","","   ","  ","  ","  ","","","","","","","","","","","1-White 2-Blue 3-Red")
    print("","","","","","","","","","","","","","","","","","","","","","","","","","","","","","   ","  ","  ","  ","","","","","","","","","","","4-yellow 5-Green 6-Purple")





 
#initializing variables
    guess_Num1 = 0
    guess_Num2 = 0
    guess_Num3 = 0
    guess_Num4 = 0
    score = 0
    Guesses = 0



# generating random numbers

    number1 = random.randrange(1, 7)
    number2 = random.randrange(1, 7)
    number3 = random.randrange(1, 7)
    number4 = random.randrange(1, 7)	



#genarating numbers to list
    Secret_Num = [number1, number2, number3, number4]


#calculating number of attempts
    attempt = 0



#processing the game
    while attempt < 8:
        attempt += 1
        print("attempt :", attempt)


#get users inputs

        while True:
            try:
                guess_Num1 = int(input("Enter first number 1-6  : "))

            except ValueError:
                print("Please enter a  number 1-6")
                continue
            if guess_Num1 >= 0 and guess_Num1 <= 6:

                break
        
#display a error
            else:
                print('The number must be in the range 1-6')


#get users inputs
        while True:
            try:
                guess_Num2 = int(input("Enter second number 1-6 : "))

            except ValueError:
                print("Please enter a  number 1-6")
                continue
            if guess_Num2 >= 0 and guess_Num2 <= 6:

                break



            else:
                print('The number must be in the range 1-6')


#get users inputs
        while True:
            try:
                guess_Num3 = int(input("Enter Third number 1-6  : "))

            except ValueError:
                print("Please enter a  number 1-6")
                continue
            if guess_Num3 >= 0 and guess_Num3 <= 6:

                break


#display a error
            else:
                print('The number must be in the range 1-6')


#get users inputs
        while True:
            try:
                guess_Num4 = int(input("Enter fourth number 1-6 : "))

            except ValueError:
                print("Please enter a  number 1-6")
                continue
            if guess_Num4 >= 0 and guess_Num4 <= 6:

                break


#display a error
            else:
                print('The number must be in the range 1-6')


# adding guessed numbers to list
        Guessed_Num = []
        Guessed_Num.append(guess_Num1)
        Guessed_Num.append(guess_Num2)
        Guessed_Num.append(guess_Num3)
        Guessed_Num.append(guess_Num4) 
 
                     
# finishing the game 

        if Guessed_Num == [0, 0, 0, 0]:
            print("Successfully Exited")
            again = input("Do you want to play another game (Yes/No) ?")
            exit()


# adding smallpegs results to a list
        smallPegs = []


# checking guessed number 1
        if number1 == guess_Num1:
            smallPegs.append("1")
            score+=2
        elif guess_Num1 in Secret_Num:
            smallPegs.append("0")
            score+=1
        else:
            smallPegs.append(".")
 
# checking guessed number 2
        if number2 == guess_Num2:
            smallPegs.append("1")
            score+=2
        elif guess_Num2 in Secret_Num:
            smallPegs.append("0")
            score+=1
        else:
            smallPegs.append(".")

# checking guessed number 3
        if number3 == guess_Num3:
            smallPegs.append("1")
            score+=2
        elif guess_Num3 in Secret_Num:
            smallPegs.append("0")
            score+=1
        else:
            smallPegs.append(".")
# checking guessed number 4
        if number4 == guess_Num4:
            smallPegs.append("1")
            score+=2
        elif guess_Num4 in Secret_Num:
            smallPegs.append("0")
            score+=1
        else:
            smallPegs.append(".")


        



# printing results
        print("Attempt No ", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
              "", "", "",  "Guess", "", "", "", "", "", "", "", "", "", "", "",
              "", "", "", "", "", "", "", "", "" "", "", "","","","","","", " Result ")
        print(attempt, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
              "", "", "", "", "", "", "", "", "", "", "", *Guessed_Num, "", "", "", "", "", "", "", "", "", "", "", "",
              "", "", "", "", "", "", "", "", "", "", "", "", "", "", *smallPegs)
        print('_' * 80)
        


 
# winning the game

        if smallPegs == ['1', '1', '1', '1']:
            print("Congratulations !!!!! You have won the game...")
            score+=500
            break
        






                
                


