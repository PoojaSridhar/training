french_words = {"les poires" : "pears",
                "les bonbons" : "sweets",
                "les pommes" : "apples",
                "les frites" : "french fries",
                "les boissons" : "drinks",
                "l'eau" : "water",
                "la nourriture" : "food"}
   

french = ["les poires", "les bonbons", "les frites", "les boissons", "les pommes", "l'eau", "la nourriture"]
removed = []

import random
import time

print("Hello and welcome to French Revision. To continue type y, to quit, type q, to add a word to the dictionary, type d.\n")
print("Here is the list of words on which you will be tested:\n")
print(french)

while True:
    if len(french) != 0:
        answer = raw_input("\nWould you like to continue? ")
        if answer != "y" and answer != "d":
            print("Please enter a valid instruction")

        elif answer == "y":
            word = random.choice(french)
            french.remove(word)
            removed.append(word)
            english = french_words[word]
            print(word)
            user_answer = raw_input("What is the english translation of the word? ")
            if user_answer.lower().strip() == english:
                print("Your answer is correct")
            else:
                print("Sorry, your answer is wrong. The correct answer is " + english)

        elif answer == "d":
            french_word = raw_input("Please add a french word that is not present in the list mentioned above and has not been added before. ")              
            translation = raw_input("Please add the english translation of the word ")
            french.append(french_word)
            french_words[french_word] = translation                
        
    else:
        print("\nYou have answered all the questions. Goodbye, the program will automatically shut after 10 seconds")
        time.sleep(10)
        break
    
#add permanently to database. while loop to check. code not long. have to do front end so attractive to users.

        
#french_words = {}
#french_words1 = open('french_words.txt')
#french_words1.read()
#for line in  french_words1:
#    (key, val) = line.split()
#    french_words[key] = val

#french_words = open('french_words.txt', 'a')
#french_words.write("\n")
#french_words.write("%s : %s" % (french_word, translation))
#french_words.close()
#french_words = open('french_words.txt')
#print(french_words.read())
    
