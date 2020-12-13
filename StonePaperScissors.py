#The aim is to build a stone paper scissors game 
#Score management with file handling included 
#done with score management
#now time for File handling
#like need to put scores in that and read that at the time of execution and load them into scores 
#putting is done
#reading is left
#Done :) 
#Really Happy because i was able to develop what I was thinking 
#With basic game added the concept of maintaining scores and saving them into file on local desktop

from random import randrange

globals()['computerScore'] = 0
globals()['userScore'] = 0 

try:
    f = open("scores.txt","r")
    strr = f.read()
    scoreList = strr.split(",")
    globals()['userScore'] = int(scoreList[0])
    globals()['computerScore'] = int(scoreList[1])

except Exception as e:
    print(e)
finally:
    f.close()


def getChoice(val):
    if val == 1:
        return "st"
    elif val == 2:
        return "pp"
    elif val == 3:
        return "sc"
    else:
        print("WRONG CHOICE  " + str(val))
        return 'error'

def getResult(cInput,userInput):
    if(cInput == "error" or userInput == "error"):
        return "Error Occured due to your choice"
    if(cInput == userInput):
        return ( "Draw, your choice was " + userInput + " And Computer's was " + cInput)
    elif(cInput == "st" and userInput == "sc"):
        pass
        #print( "Computer Won , your choice was " + userInput + " And Computer's was " + cInput)
    elif(cInput == "pp" and userInput == "st"):
        pass
        #print( "Computer Won , your choice was " + userInput + " And Computer's was " + cInput)
    elif(cInput == "sc" and userInput == "pp"):
        pass
        #print( "Computer Won , your choice was " + userInput + " And Computer's was " + cInput)
    else:
        temp = globals()['userScore']
        temp = temp + 1 
        globals()['userScore'] = temp
        return "You won , your choice was " + userInput + " And Computer's was " + cInput
    
    temp1 = globals()['computerScore']
    temp1 = temp1 + 1 
    globals()['computerScore'] = temp1
    return "Computer Won , your choice was " + userInput + " And Computer's was " + cInput


userVal = 1
while userVal != 9:
    val = randrange(1,3)
    cInput = getChoice(val)
    print("Computer choose" + str(cInput))

    userVal = int(input("Enter your choice .. \n 1 for stone \n 2 for paper \n 3 for scissors \n "))
    userInput = getChoice(userVal)
    print("User's Choice is " + str(userInput))

    print(getResult(cInput,userInput))


print("Thanks for playing...!! ")
print("Your Score is " + str(globals()['userScore']) )
print("Computer's Score is " + str(globals()['computerScore']))

try:
    f = open("scores.txt","w")
    strr = str(globals()['userScore']) + ","  + str(globals()['computerScore'])
    f.write(strr)
except Exception as e:
    print(e)
finally:
    f.close

