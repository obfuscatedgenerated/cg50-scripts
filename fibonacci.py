i = 0
j = 1

targ = float(input("Target (or type inf):\n")) # get the target number

while targ != i and i < targ: # loop until the target number is reached or exceeded
    print(i) # print the current number
    nth = i + j # calculate the next number
    i, j = j, nth # set the current number to the previous number and the next number to the current number

print(i) # print the final reached number

print(str(targ)+" in sequence: "+str(i == targ)) # print whether the target number was reached
