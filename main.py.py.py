from datetime import datetime
import random


def greet_user():
    print("Hello! I am Aira, your virtual assistant.")
    name = input("Before we begin, what is your name? ").strip()

    if not name:
        name = "Friend"

    name = name.title()
    print(f"Nice to meet you, {name}!")
    print("I'm Aira. How can I help you today?")
    return name


def show_quote():
    quotes = [
        "Believe in yourself and keep going!",
        "Small steps every day lead to big results.",
        "Your only limit is your mindset.",
        "Every expert was once a beginner.",
        "Don't give up. Great things take time."
    ]
    print("Aira:", random.choice(quotes))


def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the computer cold? It left its Windows open!",
        "Why do Python programmers wear glasses? Because they cannot C!"
    ]
    print("Aira:", random.choice(jokes))


def tell_fact():
    facts = [
        "Honeybees communicate using a dance.",
        "Octopuses have three hearts.",
        "The Moon is slowly moving away from Earth.",
        "A day on Venus is longer than its year.",
        "Sharks existed before trees."
    ]
    print("Aira:", random.choice(facts))


def calculator():
    """Perform basic arithmetic and handle invalid input safely."""
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))

    except ValueError:
        print("Aira: Please enter valid numbers.")
        return

    if operator == "+":
        print("Aira:", num1 + num2)
    elif operator == "-":
        print("Aira:", num1 - num2)
    elif operator == "*":
        print("Aira:", num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("Aira: Cannot divide by zero!")
        else:
            print("Aira:", num1 / num2)
    else:
        print("Aira: Invalid operation. Use +, -, *, or /.")

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("Aira: Guess a number between 1 and 10!")
    print("You have 3 attempts.")

    while attempts > 0:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Aira: Please enter a whole number!")
            continue

        if guess < 1 or guess > 10:
            print("Aira: Choose a number between 1 and 10!")
            continue

        if guess == secret_number:
            print("Aira: Correct! You won!")
            return
        elif guess < secret_number:
            print("Aira: Too low!")
        else:
            print("Aira: Too high!")

        attempts -= 1

    print("Aira: Game over! The number was", secret_number)

def recommend_activity():
    """Recommend an activity based on the current time of day."""
    hour = datetime.now().hour

    if 5 <= hour < 12:
        activity = "Good morning! Plan your day and start with your most important task."
    elif 12 <= hour < 17:
        activity = "It's afternoon! Take a short break, have some water, and review your progress."
    elif 17 <= hour < 21:
        activity = "It's evening! Consider exercising, learning a skill, or enjoying a hobby."
    else:
        activity = "It's late! Wind down, prepare for tomorrow, and get enough rest."

    print("Aira:", activity)

def perceptron_demo():
    """Demonstrate a simple, non-trained perceptron calculation."""
    print("Aira: Let's try a simple perceptron!")

    try:
        input1 = int(input("Enter input 1 (0 or 1): "))
        input2 = int(input("Enter input 2 (0 or 1): "))

        if input1 not in [0, 1] or input2 not in [0, 1]:
            print("Aira: Invalid input! Please enter only 0 or 1.")
            return

    except ValueError:
        print("Aira: Invalid input! Please enter only 0 or 1.")
        return

    weight1 = 0.5
    weight2 = 0.5
    bias = -0.7

    total = (input1 * weight1) + (input2 * weight2) + bias

    if total >= 0:
        output = 1
    else:
        output = 0

    print("Aira: Weighted total =", total)
    print("Aira: Perceptron output =", output)

def show_help():
    print("Aira: Here are my commands:")
    print("- hello or hi: Greet you")
    print("- name: Tell you my name")
    print("- my name: Tell you your name")
    print("- time: Show the current time")
    print("- date: Show today's date")
    print("- calculator: Perform calculations")
    print("- activity: Get a time-based activity recommendation")
    print("- perceptron: Demonstrate a simple perceptron calculation")
    print("- quote: Give a motivational quote")
    print("- joke: Tell a joke")
    print("- fact: Tell a random fact")
    print("- game: Play a number-guessing game")
    print("- thanks: Say thank you")
    print("- ok: Acknowledge you")
    print("- help: Show available commands")
    print("- bye, exit, or quit: End the conversation")


def main():
    name = greet_user()

    while True:
        command = input("You: ").strip().lower()

        if command in ["hello", "hi", "hey"]:
            print(f"Aira: Hi, {name}! How can I help you?")

        elif command == "name":
            print("Aira: My name is Aira.")

        elif command == "my name":
            print(f"Aira: Your name is {name}!")

        elif command == "time":
            current_time = datetime.now().strftime("%I:%M:%S %p")
            print(f"Aira: The current time is {current_time}.")

        elif command == "date":
            current_date = datetime.now().strftime("%d %B %Y")
            print(f"Aira: Today's date is {current_date}.")

        elif command == "activity":
            recommend_activity()

        elif command == "perceptron":
            perceptron_demo()

        elif command == "calculator":
            calculator()

        elif command == "quote":
            show_quote()

        elif command == "joke":
            tell_joke()

        elif command == "fact":
            tell_fact()

        elif command == "game":
            play_game()

        elif command == "thanks":
            print(f"Aira: You're welcome, {name}!")

        elif command == "ok":
            print(f"Aira: Alright, {name}!")

        elif command == "help":
            show_help()

        elif command in ["bye", "exit", "quit"]:
            print("Aira: Goodbye! Have a great day.")
            break

        else:
            print("Aira: I don't understand that command yet. Type 'help' to see my commands.")


if __name__ == "__main__":
    main()