import random
# Using 'While Loop' to run the game over and over until the user decides to quit
c= True
while c == True:
    # Words list
    words = ['gamer', 'computer', 'cat', 'ball', 'games', 'player', 'bread', 'banana', 'cabbage', 'witcher', 'red', 'redemption', 'table', 'chair',
             'television', 'oranges', 'football', 'cricket', 'guava', 'watermelon', 'cooler', 'fan', 'song', 'phone', 'tablet', 'wire', 'cable', 'car', 
             'boy', 'girl', 'star', 'moon','earth', 'world', 'mars', 'perseverance', 'curiosity', 'ecstasy', 'easy', 'hard', 'garden', 'grand', 'theft', 
             'auto', 'machine', 'artificial', 'intelligence', 'knowledge','plethora', 'honda', 'porsche', 'audi', 'toyota', 'lamborghini', 'tesla', 'windows', 
             'pascal', 'einstein', 'newton', 'microsoft', 'apple', 'android', 'google', 'facebook', 'python', 'pycharm',
             'graphics', 'youtube']
    # Choosing a random word
    word = random.choice(words)
    # Finding the length of the word and printing it to let user know
    num_of_ltrs = str(len(word))
    print("It is a/an "+ num_of_ltrs +" letters' word")
    # Creating an empty list of dashes
    empty = []
    for i in range (0, int(num_of_ltrs)):
        empty.append('_')
    # Giving the user guesses
    guesses = 5
    # Using 'While Loop' to give the player some guesses till the game is over
    while guesses != 0:
        # Prompting the user to guess and input a letter
        print ("Guess a letter: ")
        ltr=input()
        # Checking if the letter is in the word and showing its location
        if ltr in word:
            pos = word.index(ltr)
            position = pos+1
            print(f"Yes it is in the {position} th place")
            empty[pos] = ltr
            for i in range (0, int(num_of_ltrs)):
                print (empty[i], end='')
            # Giving the player a chance to guess the result based on his current assumption
            print("\nNow try to guess the word: ")
            trial = input()
            # Checking if the word is correct
            if trial == word:
                # Congratulating the winner if he guesses correctly and breaking the loop
                print("You have guessed the word correctly! Congratulations!")
                break
            else:
                # Showing if the guessed word is wrong
                print("That's not the word.")
        else:
            # Player failed to guess a correct letter and lost a guess
            guesses = guesses -1
            print(f"You have {guesses} guesses left")
    # Showing the player he failed when he lost all guesses
    if guesses == 0:
        print(f"You lost! :( \nThe word was {word}")
    print("Do you want to play again? Answer Yes or No")
    ans = input()
    if ans == 'No' or ans == 'no':
        c= False
    else:
        c=True
print("Thanks for playing guess the word..........©Sabbir_Ahmed2021")

