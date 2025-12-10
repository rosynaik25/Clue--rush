import random


categories = {
    "animals": {
        "elephant": ["I am one of the heaviest land animals", "I have large ears", "I use my trunk for many tasks"],
        "tiger": ["I am a carnivore", "I have orange fur with stripes", "I am found in Asia"],
        "giraffe": ["I eat leaves from tall trees", "I have a long neck", "I am the tallest land animal"],
        "zebra": ["I live in groups on grasslands", "I have black-and-white stripes", "I am related to horses"],
        "panda": ["I mostly eat bamboo", "I am black and white", "I am native to China"],
        "kangaroo": ["I move by hopping", "I carry my baby in a pouch", "I am commonly found in Australia"]
    },

    "fruits": {
        "apple": ["I can be red, green, or yellow", "I grow in cooler climates", "A famous saying involves me and doctors"],
        "banana": ["I am long and curved", "I am rich in potassium", "Monkeys love me"],
        "mango": ["I am called the king of fruits", "I am sweet and juicy", "I am popular in tropical regions"],
        "orange": ["I am rich in Vitamin C", "I have a tangy taste", "I share my name with a color"],
        "grapes": ["I grow in bunches", "I can be green, red, or black", "I am used to make juices"],
        "pineapple": ["I have a hard, spiky outside", "I am juicy and yellow inside", "I grow on the ground, not trees"]
    },

    "places": {
        "india": ["I am in South Asia", "World's largest democracy", "Its currency features Mahatma Gandhi."],
        "france": ["Known for fashion and art", "Eiffel Tower is here", "My capital is Paris"],
        "japan": ["Famous for technology", "Known as the Land of the Rising Sun", "Origin of bullet trains."],
        "egypt": ["I have ancient pyramids", "The Nile flows through me", "A famous stone helped translate its old language."],
        "brazil": ["I am famous for football", "Amazon rainforest is here", "My capital is Brasília"],
        "canada": ["I am known for maple syrup", "I have huge forests and lakes", "Has the world’s longest bi-national border."]
    }
}
name=input("Enter you name :")
print(name,"! \nWelcome to the CLUE-RUSH Game!")

while True:
    print("\nAvailable Categories:")
    for cat in categories:
        print(f"- {cat}")

    chosen_cat = input("\nEnter a category name: ").lower()

    if chosen_cat not in categories:
        print("❌ Invalid category. Try again!")
        continue

    items = categories[chosen_cat]
    word = random.choice(list(items.keys()))
    hints = items[word]

    score = 0
    print("\nYou chose: ",chosen_cat.upper())
    print("You will get 3 hints.")
    print("Scoring: Hint 1 = 30 pts, Hint 2 = 20 pts, Hint 3 = 10 pts.\n")

    
    for i in range(3):
        print(f"Hint {i+1}: {hints[i]}")
        guess = input("Your guess: ").lower()

        if guess == word:
           
            if i == 0:
                points = 30
            elif i == 1:
                points = 20
            else:
                points = 10

            score += points
            print(" Correct! You earned ",points,"points!")
            break
        else:
            print("❌ Wrong guess!\n")

    if guess != word:
        print(" You couldn't guess it. The answer was:",word)

    print(" Your score this round: ",score, "points")

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\n Thanks for playing! Goodbye!")
        break

