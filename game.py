import time

def welcome_player():
    print("Do you want to play as a user or a guest?")
    choice = input("Enter 'user' or 'guest': ").strip().lower()
    
    if choice == "user":
        name = input("Enter your name: ")
    else:
        name = "Guest"
    
    print(f"Welcome, {name}!")
    return name

def countdown():
    print("Starting game in:")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

def play_game():
    gospels = {
        "matthew": "Correct! This is the first book of the Gospels.",
        "mark": "Correct! This is the second book of the Gospels.",
        "luke": "Correct! This is the third book of the Gospels.",
        "john": "Correct! This is the fourth book of the Gospels."
    }
    attempts = 3
    
    print("The Gospels are four:")
    print("1. Matthew\n2. Mark\n3. Luke\n4. John")
    
    while attempts > 0:
        answer = input("Which Gospel book would you like to guess? ").strip().lower()
        
        if answer in gospels:
            print(gospels[answer])
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong! This is not a Gospel. You have {attempts} more attempts.")
            else:
                print("Wrong! This is not a Gospel. You have exhausted all options.")
                break

def main():
    while True:
        name = welcome_player()
        ready = input("Are you ready to play? (yes/no): ").strip().lower()
        
        if ready == "no":
            exit_choice = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if exit_choice == "yes":
                countdown()
                print("Goodbye!")
                break
        
        countdown()
        play_game()
        
        replay = input("Would you like to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
