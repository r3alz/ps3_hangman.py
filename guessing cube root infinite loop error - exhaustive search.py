x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    print("infinite loop") #this is to show that there is an inifite loop.  
#infinite loop becuase guess will always be < x in this example.  the if statement will end at a certain point because /
#abs(guess**2 - x) will eventually be < epsilon, so guess will stop at a certain point and never be greater than x.
    if abs(guess**2 -x) >= epsilon:
        guess += step
        print(guess)
    

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
