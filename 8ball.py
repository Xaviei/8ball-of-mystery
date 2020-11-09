#import random for random selection of buttons
import random
#Function getAnswer actual function
def getAnswer(answerNumber):
    if answerNumber == 1: #copy and pasted if elif statements for diffrent randomly selected outcomes
        return 'it is certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'A little hazy, try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'concentrate and ask again'
    elif answerNumber == 7:
        return 'I have to  say no'
    elif answerNumber == 8:
        return 'Outlook is not so good'
    elif answerNumber == 9:
        return 'very doubtful'
#random. randint command choosing a number 1-9
#function fortune being passed so that if applied in function it allows for getAnswer funtion to be used
print(getAnswer(random.randint(1, 9)))

