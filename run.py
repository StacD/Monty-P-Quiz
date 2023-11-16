"""
Welcome Message.
"""
print("Welcome to this Monty Python Quiz!\n")
print("Select A, B or C for your answer then press enter.\n")
print("First answer only is accepted!\n")

questions = ("Nobody expects what historic event?\n",
    "Michael Palin seeks out John Cleese to have what type of conflict?\n",
    "“He’s not the Messiah, he’s a very naughty boy.” Comes from what film?\n",
    "Which Monty Python member appears in the Harry Potter films?\n",
    "The Pythons debuted with what TV show?\n",
    "The Pythons released what sketch-based movie in 1983?\n",
    "What sketch about canned meat gave us the nickname for junk email?\n",
    "What was the third movie done by the Pythons?\n",
    "What Python musical debuted on Broadway in 2005?\n",
    "Monty Python & the Holy Grail was shot mostly in what country?\n"
    )

options = (("A. The Spanish Inquisition", "B. The Plague", "C. The Ice Age"),
           ("A. A heated discussion", "B. An argument", "C. A fight"),
           ("A. Life of Brian", "B. The Meaning of Life", "C. The Holy Grail"),
           ("A. Terry Gilliam", "B. Michael Palin", "C. John Cleese"),
           ("A. The Goons", "B. Monty Pythons Flying Circus", "C. Q8"),
           ("A. Monty Python!", "B. The Holy Grail", "C. The Meaning of Life"),
           ("A. Spam", "B. Ham", "C. Corn Beef"),
           ("A. The Holy Grail", "B. Python One", "C. Life of Brian"),
           ("A. Bright Side of Life", "B. Spamalot", "C. Life of Brian"),
           ("A. Wales", "B. Scotland", "C. France")
           )

answers = ("A", "B", "A", "C", "B", "C", "A", "C", "B", "B")
guesses = []
score = []


def play_quiz():
    question_num = 0
    score = 0
    for question in questions:
        print("--------------------")
    for option in options[question_num]:
        print(option)
        guess = input("\nEnter (A, B or C): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("\nCorrect!")
        elif guess != answers[question_num] and guess in (answers):
            print("\nIncorrect")
        else:
            guess not in (answers)
            print("Invalid input, please select A, B, C")
        question_num += 1
        continue


def play_again():
    while True:
        user_response = input.guess("Would you like to try again? (yes / no): ")
        if user_response == "yes":
            return True
        elif user_response == "no":
            print("\nThankyou for playing. Have a nice day!")
            break
        else:
            print("Please type 'yes' or 'no'")
            continue

print("-----RESULT!-----")
print("You got " + str(score) + " / 10 correct!\n")

play_quiz()

while play_quiz():
    play_quiz()
