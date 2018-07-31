def hangman():
    import random
    def word():
        words = ["hello", "complex","shelter","pinch","canvas","sin","fade","refused",
        "rain","adamant","face","venomous","mark","parched","possess","teeth",
        "building","love","gaudy","modern","ruthless","jumpy","remarkable",
        "colour","jeans"]
        for w in words:
            phrases = random.choice(words)
        return phrases
    def text(phrase,guessed):
        display = ""
        for letter in phrase:
            if letter in guessed:
                display += letter
            elif letter == " ":
                display += "  "
        #the letter in our phrase has not been guessed yet
            else:
                display += "_ "
        return display

    #tell user how many spaces and letters:
    def main():
        game_over = False
        phrase = word()
        guessed = []
        text2 = text(phrase,guessed)
        print(text2)
        while game_over != True:
            guess = input("Enter a letter: ")
            guessed.append(guess)
            text3 = text(phrase,guessed)
            print(text3)
            if "_ " in text3:
                game_over = False
            else:
                game_over = True

        print("You did it! The answer was {}".format(phrase))
    if __name__ == "__main__":
        main()
