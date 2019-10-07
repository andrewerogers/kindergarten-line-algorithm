## Variables
length = 100 ## length of line
kLine = [0]*length ## initializing array of all 0
MAX_ITERATIONS = 60 ## number of iterations
j = 0 ## while loop iterant

## importing random library to make random modulus
from random import randrange

## Assigning random values to array
for i in range(length):
    kLine[i] = randrange(0,2)

## print function
def printArray(kLine):
    for i in range(length):
        print(kLine[i])

## printing initial state
print("Initial State: ")
printArray(kLine)

## Modeling line behavior

while j < MAX_ITERATIONS:
    for i in range(length):
        if(i == length-1):
            break;
        ## if students are facing each other turn around
        if(kLine[i] == 1 and kLine[i + 1] == 0):
            kLine[i] = 0
            kLine[i+1] = 1
            i+=1
    j+=1

## printing final state after line behavior
print()
print("Final State: ")
printArray(kLine) 

