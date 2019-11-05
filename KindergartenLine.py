## Notice the variable MAX_ITERATIONS is set to .6*length, this does
## not work for worst case runtime but it does for average case runtime.

length = 1000 ## length of line
kLine = [0]*length ## initializing array of all 0's
MAX_ITERATIONS = .6*length ## number of iterations
j = 0 ## while loop index

## importing random library to make random modulus
from random import randrange

## Assigning random values to array
for i in range(length):
    kLine[i] = randrange(0,2)

## print function
def printArray(kLine):
    for i in range(length):
        print(kLine[i],end='')

## printing initial state
print("Initial State: ")
printArray(kLine)


## modeling line behavior
## the while loop is included to make it
## easy to vary the number of passes

while j < MAX_ITERATIONS:
    for i in range(length - 1):
        ## if students are facing each other turn around
        if(kLine[i] == 1 and kLine[i + 1] == 0):
            kLine[i] = 0
            kLine[i+1] = 1
            i+=1 ## increment i again to avoid data overwrite

    j+=1

## printing final state after line behavior
print()
print("Final State: ")
printArray(kLine) 

