def multiply(a, b):
    total = 0
    for i in xrange(1, (b+1)):
        total += a
    return total


def divide(p, q):
    while p < q:
        print("p has to be greater than or equal to q")
        break
            
    else:
        ans = float(p) / float(q)
        rem = (ans - int(p/q)) * q
        print(int(ans))
        print(int(rem))

        

def divide1(p, q):
    while p < q:
        print("p has to be greater than or equal to q")
        break
    
    else:
        ans = p / q
        rem = p - (ans * q)
        print(ans)
        print(rem)

        
    
        
def tables():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for number in numbers:
        for i in xrange(1, 13):
            print("{} {} {} {} {}").format(number, "*", i, "=", number*i)



import random
number2 = random.randint(1, 100)
print("I've picked a random number between 1 and 100, can you guess which one it is?")

for i in range(1, 11):
    guess = input("> ")
    if guess > number2:
        if i < 10:
            print("That's too high!, try again")
    elif guess < number2:
        if i < 10:
            print("That's too low!, try again")
    else:
        print("That's it! Your guess is correct")
        break
else:
    print("Game Over")
    print("The correct answer was " + str(number2))

    




    
