import random

def display_rules():
    print("Rock vs paper->paper wins")
    print("Rock vs scissors->Rock wins")
    print("Paper vs scissors->scissors wins")

def get_user_choice():
    valid_choices = ['r', 'p', 's']
    while True:
        user_input = input("Choose Rock (r), Paper (p), or Scissors (s): ").lower()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    choices = ['r', 'p', 's']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        return "user"
    else:
        return "computer"

def display_winner(winner, user, computer):
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print(f"You win! {get_choice_name(user)} beats {get_choice_name(computer)}")
    else:
        print(f"Computer wins! {get_choice_name(computer)} beats {get_choice_name(user)}")

def get_choice_name(choice):
    if choice == 'r':
        return "Rock"
    elif choice == 'p':
        return "Paper"
    else:
        return "Scissors"

def update_score(winner, user_score, computer_score):
    if winner == "user":
        user_score += 1
    else:
        computer_score += 1
    return user_score, computer_score

def main():
    display_rules()
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_winner(winner, user_choice, computer_choice)
        user_score, computer_score = update_score(winner, user_score, computer_score)
        print(f"Score: User {user_score} - Computer {computer_score}")
        print("Do you want to play again? (Y/N)")
        ans = input().lower()
        if ans != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()