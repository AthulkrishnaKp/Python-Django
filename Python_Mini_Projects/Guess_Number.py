import random

# def guess(x):
#     random_num=random.randint(1,x)
#     guess=0
#     while guess != random_num:
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess <= random_num:
#             print("Sorry, Guess again. Too low.")
#         if guess >= random_num:
#             print("Sorry, Guess again. Too high.")
#     print(f'yah, congrats. You have guessed the number {random_num} correctly')
#
# guess(10)


def computer_guess(x):
    low=1
    high=x
    user=""
    while user != "c":
        guess = random.randint(low, high)
        user = input(f"Is {guess} too high (H), too low (L), or correct (c) : ")
        if user == 'h':
            high=guess-1
        elif user == 'l':
            low=guess+1
    print(f"Yah, The computer guessed my number, {guess} correctly")

computer_guess(1000)