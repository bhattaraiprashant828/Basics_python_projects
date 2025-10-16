# Dice Rolling Game. 
# import random
# choise=str(input("ROll a dice (y/n): "))
# if choise=='y':
#     dice=random.randint(1,6)
#     print((f"The dice flip to {dice} "))
# elif choise=='n':
#     print("Thanks for Playing")

# else:
#     print("Invalid Choise")


# Coin Tossing  Game. 
# import random
# options=["head","tail"]
# choice=(input("Will you toss a Coin ? (yes/no): ")).strip().upper().lower()
# if choice=='y':
#     toss=random.choice(options)
#     print(f"The coin has flip to the air and it is  {toss}")
# elif choice=='n':
#     print("Thanks!  But you have to choise yes for playing. ")
# else:
#     print("Invalid choise")


# Number Guessing Game.
# import random
# num=random.randint(1,5)
# try:
#     guess=int(input("Guess a Number between (1-5) "))
#     if num==guess:
#         print(f"Wow! Your guess is correct that is exactly {guess}")
#     else:
#         print(f" Sorry! Your guess is incorect , The correct number was {num} ")
# except ValueError:
#     print("Please! Enter a valid number between (1-5). ")


# Rock , Paper and Scissors Game.
# import random
# options=['rock','paper','scissors']
# full_names={'r':'rock','p':'papers','s':'scissors'}
# user_choises=input("Rock, Paper, or Scissors (r/p/s): ").lower()
# if user_choises not in options:
#     print("Invalid choise! ")
# else:
#     friends_choises=random.choice(options)

#     print(f"Your choise is {user_choises}")
#     print(f"Friend choise is {friends_choises}")

#     if user_choises==friends_choises:
#         print("It's Tie, Please Try Again!")
#     elif (
#         (user_choises=="r" and friends_choises=="s") or
#         (user_choises=="s" and friends_choises=="p") or
    #     (user_choises=="p" and friends_choises=="r")
    #     ):

    #     print("Congrats You win! ")
    # else:
    #     print("Friend wins! ")


# Generating QR Code. 
# import qrcode
# info=input("Enter text or URL : ").strip()
# name=input("Enter the filename : ").strip()
# img=qrcode.make()
# img.save(name)
# print(f"QR code saved as {name} ")


# Currency Converters.
# import requests
# def currency_converter():
#     url = "https://api.exchangerate-api.com/v4/latest/USD"
#     response = requests.get(url)
#     data = response.json()
    
#     print("Currency rates:", data["rates"])
#     amount = float(input("Enter amount in USD: "))
#     target_currency = input("Enter target currency (e.g., EUR , NPR): ").upper()
    
#     if target_currency in data["rates"]:
#         converted_amount = amount * data["rates"][target_currency]
#         print(f"{amount} USD is equal to {converted_amount} {target_currency}.")
#     else:
#         print("Invalid currency code.")

# currency_converter()



# def quiz_game():
#     questions = {
#         "What is the capital of France?": "paris",
#         "Who wrote 'Hamlet'?": "shakespeare",
#         "What is the largest planet in our solar system?": "jupiter"
#     }
    
#     score = 0
#     for question, answer in questions.items():
#         user_answer = input(question + " ").lower()
#         if user_answer == answer:
#             score += 1
#             print("Correct!")
#         else:
#             print(f"Wrong! The correct answer is {answer}.")
    
#     print(f"Your score: {score}/{len(questions)}")

# quiz_game()


# Generate a Random Password.
# import random
# import string

# def generate_password():
#     length = int(input("Enter password length: "))
#     all_chars = string.ascii_letters + string.digits + string.punctuation +string.punctuation
#     password = ''.join(random.choice(all_chars) for _ in range(length))
#     print(f"Your Generated password is : {password}")
# generate_password()

# Password Checkers.
# import re
# def check_password_strength():
#     password = input("Enter your password: ")
    
#     if len(password) < 8:
#         print("Password is too short! It must be at least 8 characters.")
#     elif not re.search(r"[A-Z]", password):
#         print("Password must contain at least one uppercase letter.")
#     elif not re.search(r"[a-z]", password):
#         print("Password must contain at least one lowercase letter.")
#     elif not re.search(r"[0-9]", password):
#         print("Password must contain at least one digit.")
#     elif not re.search(r"[@$!%*?&]", password):
#         print("Password must contain at least one special character.")
#     else:
#         print(f"Your Password {password} is strong and you can set it.")

# check_password_strength


# class ATM:
#     def __init__(self):
#         self.balance = 1000
    
#     def deposit(self):
#         amount = float(input("Enter deposit amount: "))
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")
    
#     def withdraw(self):
#         amount = float(input("Enter withdrawal amount: "))
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds.")
    
#     def check_balance(self):
#         print(f"Current balance: {self.balance}")
    
# def atm_simulation():
#     atm = ATM()
    
#     while True:
#         print("\nATM Menu: \n1. Deposit \n2. Withdraw \n3. Check Balance \n4. Exit")
#         choice = input("Choose an option: ")
        
#         if choice == "1":
#             atm.deposit()
#         elif choice == "2":
#             atm.withdraw()
#         elif choice == "3":
#             atm.check_balance()
#         elif choice == "4":
#             print("Thank you for operating with us.")
#             break
#         else:
#             print("Invalid option, please try again.")

# atm_simulation()


# import time
# start_time=time.time()
# typed_text=str(input("Start typing the word : "))
# end_time=time.time()
# time_taken=(end_time -start_time)/60.0
# words=int(len(typed_text))
# print(f"You have typed total {words} characters. ")
# print(f"Total time taken {time_taken:.2f} min for typing")
# wpm=words/time_taken
# print(f"Your speed is {wpm:.2f} WPM")


# import time

# def wpm_calculator():
#     # Sentence to type
#     test_sentence = ("The sun was setting behind the mountains, casting a golden glow over the valley. A cool breeze rustled the leaves of the trees, creating a peaceful melody that filled the air. Birds flew across the sky, their wings cutting through the warm evening light.")
#     print("Type the following sentence as fast and accurately as you can:\n")
#     print(test_sentence)
#     input("Press Enter when you are ready to start...")

#     # Start timer
#     start_time = time.time()
#     typed_text = input("\nStart typing here:\n")
#     end_time = time.time()

#     # Calculate time taken
#     time_taken = end_time - start_time
#     time_in_minutes = time_taken / 60

#     # Count words
#     word_count = len(typed_text.split())

#     # Calculate WPM
#     wpm = word_count / time_in_minutes if time_in_minutes > 0 else 0

#     # Calculate accuracy
#     correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(test_sentence) and c == test_sentence[i])
#     accuracy = (correct_chars / len(test_sentence)) * 100

#     # Results
#     print("\n--- Results ---")
#     print(f"Time taken: {time_in_minutes:.2f} seconds")
#     print(f"Your typing speed: {wpm:.2f} words per minute")
#     print(f"Accuracy: {accuracy:.2f}%")

# # Run the program
# wpm_calculator()
















































































































































































































































































