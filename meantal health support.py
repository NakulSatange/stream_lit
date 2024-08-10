# mental_health_support.py

def display_welcome_message():
    print("Welcome to the Mental Health Support App.")
    print("I'm here to offer some supportive advice based on your input.")
    print("Remember, this is not a substitute for professional help.")

def get_user_input():
    print("\nHow are you feeling today?")
    print("1. Anxious")
    print("2. Depressed")
    print("3. Stressed")
    print("4. Overwhelmed")
    print("5. Other")

    choice = input("Please enter the number corresponding to your feeling: ")
    return choice

def provide_support(choice):
    if choice == '1':
        print("\nIt's okay to feel anxious. Try taking deep breaths, and consider mindfulness exercises or talking to someone you trust.")
    elif choice == '2':
        print("\nDepression is serious. Please reach out to a mental health professional or counselor. Talking to friends or family can also help.")
    elif choice == '3':
        print("\nStress management techniques such as regular exercise, meditation, and relaxation can be beneficial. Don’t hesitate to seek professional advice.")
    elif choice == '4':
        print("\nFeeling overwhelmed can be challenging. Try breaking tasks into smaller steps and take regular breaks. Reach out for support if needed.")
    elif choice == '5':
        print("\nIt's okay to have unique feelings. Try to identify what specifically is bothering you and consider seeking professional advice.")
    else:
        print("\nInvalid input. Please select a valid option.")

def main():
    display_welcome_message()
    user_choice = get_user_input()
    provide_support(user_choice)

if __name__ == "__main__":
    main()
