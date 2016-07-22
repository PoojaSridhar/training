Python 2.7.10 (default, Oct 23 2015, 19:19:21) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

french_words = {"les poires" : "pears",
...                 "les bonbons" : "sweets",
...                 "les pommes" : "apples",
...                 "les frites" : "french fries",
...                 "les boissons" : "drinks",
...                 "l'eau" : "water",
...                 "la nourriture" : "food"}

french = ["les poires", "les bonbons", "les frites", "les boissons", "les pommes", "l'eau", "la nourriture"]


import random

while True:
...     answer = raw_input("Would you like to continue? ")
...     if answer == "y":
...         word = random.choice(french)
...         english = french_words[word]
...         print(word)
...         answer2 = raw_input("What is the English translation of the word? ")
...         if answer2.lower() == english:
...             print("Your answer is correct")
...         else:
...             print("Sorry, your answer is wrong. The correct answer is " + english)
...         answer3 = raw_input("Would you like to add a word to the dictionary? ")
...         if answer3 == "y":
...             answer4 = raw_input("Please add a French word ")
...             answer5 = raw_input("Please add the English translation of the word ")
...             french.append(answer4)
...             french_words[answer4] = answer5
...         else:
...             word = random.choice(french)
...             english = french_words[word]
...             print(word)
...             answer2 = raw_input("What is the English translation of the word? ")
...             if answer2.lower() == english:
...                 print("Your answer is correct")
...             else:
...                 print("Sorry, your answer is wrong. The correct answer is " + english)
...     else:
...         break
