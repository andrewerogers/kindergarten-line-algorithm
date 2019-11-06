## Notice the variable numIterations can be changed to investigate
## the number of iterations required by the algorithm

length = 100 ## length of line
kLine = [0]*length ## initializing array of all 0's
numIterations = 100 ## number of iterations


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
## prints each behavior change

for j in range(numIterations):
    k = 0 ## reset while loop index to start at front of line
    while k < length - 1:
        ## if students are facing each other turn around
        if(kLine[k] == 1 and kLine[k + 1] == 0):
            kLine[k] = 0
            kLine[k+1] = 1
            k+= 1 ## increment i again to avoid data overwrite
            
            ## as algorithm is O(n^2) comment out for large n
            ##print() ## print the behavior change
            ##print("Behvaior Change: ") 
            ##printArray(kLine)
            
        k+=1

## printing final state after line behavior
print()
print("Final State: ")
printArray(kLine) 
