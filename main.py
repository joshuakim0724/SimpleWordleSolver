guess = ""
feedback = ""
guess_list = []
MAX_WORD_LENGTH = 5
MAX_GUESS_LENGTH = 6

if __name__ == '__main__':
    try:
        with open('wordlist.txt') as f:
            for line in f:
                guess_list.append(line.strip())
    except FileNotFoundError:
        print("file not found")

    print("Good starter words are: crate, trace, slate, crane")

    for guesses in range(MAX_GUESS_LENGTH):
        invalid_response = True
        while invalid_response:
            guess = input("word:").lower()
            if len(guess) == 5:
                invalid_response = False
            else:
                print(guess, "is not a valid input. It can only be of length", MAX_WORD_LENGTH)
        print("g - green, y - yellow, w - grey (5 Total Inputs i.e. gywww)")
        invalid_response = True
        while invalid_response:
            feedback = input("Result:").lower()
            allowed_characters = "gyw"
            if len(feedback) == 5 and all(ch in allowed_characters for ch in feedback):
                invalid_response = False
            else:
                print(feedback, "is not a valid input. Please input characters g, y, w only with a length of 5")
        if feedback == "ggggg":
            print("Word Found. Total Guesses", guesses + 1)
            break

        tuple_list = tuple(guess_list)
        for word in tuple_list:
            for i in range(MAX_WORD_LENGTH):
                if feedback[i] == "w" and guess[i] in word:
                    guess_list.remove(word)
                    break
                elif feedback[i] == "g" and guess[i] != word[i]:
                    guess_list.remove(word)
                    break
                elif feedback[i] == "y" and guess[i] not in word:
                    guess_list.remove(word)
                    break
                elif feedback[i] == "y" and guess[i] == word[i]:
                    guess_list.remove(word)
                    break

        count = 0
        for word in guess_list:
            if word == guess_list[-1]:
                print(word)
            else:
                print(word, end=", ")
            count += 1
            if count == 5:
                print("")
                count = 0
