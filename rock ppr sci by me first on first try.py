import random
your_hand = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors: "))
ai_hand = random.randint(0, 2)
result = [ai_hand]

rock = 0
paper = 1
scissors = 2


if your_hand == rock and ai_hand == rock:
    print(f"AI chose {result} its a draw")
elif your_hand == rock and ai_hand == paper:
    print(f"Ai chose {result}, you lose")
elif your_hand == rock and ai_hand == scissors:
    print(f"ai chose {result}, you win.")
elif your_hand == paper and ai_hand == rock:
    print(f"ai chose {result}, you win!")
elif your_hand == paper and ai_hand == paper:
    print(f"ai chose {result}, its a draw.")
elif your_hand == paper and ai_hand == scissors:
    print(f"ai chose {result}, you lose.")
elif your_hand == scissors and ai_hand == rock:
    print(f"ai chose {result}, you lose.")
elif your_hand == scissors and ai_hand == paper:
    print(f"ai chose {result}, you win!")
elif your_hand == scissors and ai_hand == scissors:
    print(f"ai chose {result}, its a draw.")

# HOLY CARP !!! i actually did this program by myself , in the first try , without any errors !!!!!!!!!
