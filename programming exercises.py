           
def multiply(a, b):
    total = 0
    for i in range(1, (b+1)):
        total += a
    return total
        


def divide(p, q):
    if p >= q:
        ans = float(p) / float(q)
        rem = (ans - int(p/q)) * q
        print(int(ans))
        print(int(rem))
    else:
        print("p has to be greater than or equal to q")


def tables():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for number in numbers:
        for number1 in numbers1:
            print(str(number) + " * " + str(number1) + " = " + str(number * number1))
            print("\n")



import random
number2 = random.randint(1, 100)
print("I've picked a random number between 1 and 100, can you guess which one it is?")
    
list1 = []
for i in range(1, 11):
    guess = input("> ")
    list1.append("x")
    if guess > number2:
        if len(list1) < 10:
            print("That's too high!, try again ")
    elif guess < number2: 
        if len(list1) < 10:
            print("That's too low!, try again ")
    else:
        print("That's it! Your guess is correct")
        break
else:
    print("Game Over")
    print("The correct answer was " + str(number2))
















