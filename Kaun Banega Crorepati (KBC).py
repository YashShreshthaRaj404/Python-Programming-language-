import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Inroductions....
intro = print("Kaun Banega Crorepati (KBC)".center(45)
              )
intro1 = print("Welcome to the Kaun Banega Crorepati (KBC) Game".center(12))
print()

#Entry intruduction...
name = input("what is Your Name-\n")
greeting = print("Hello,",name,"Welcome to the  Kaun Banega Crorepati (KBC) Game")
# end ..
print()
# want to enter or not ??
st1 = print("Start the Game OR Go Back the Game-")
st = input()
if (st == "Start"):
    print("Lets Go!!")
else:
    print("Thank You for joining!!")
    breakpoint()
# Instructions...
print()
print("Instructions:-")
print()
print("All question are compulsory")
print("Their are total 10 questions")
print("Total prize are 10 crore")
print("All question have points and price will be given accordingly.")
print()

# Read out or next...
st2 = input("Continue ? Yes or No\n")
print()
if (st2 == "No"):
        breakpoint()
else:
     ConnectionRefusedError
print()
# Set the prize pool based on score
score = 0
# Set the total score
prize = 0
total_score = score # 100 score
total_prize = prize # 100 prize
questions = [
    {
        "question": "Q - Current Railway Minister of India is -",
        "options": ["A. Mamta Banarjee", "B. Ram Vilash", "C. Ashwini vaishnaw", "D. Piyush Goyal"],
        "answer": "C"
    },
    # Add more questions here...
]

# Randomly select a question
selected_question = random.choice(questions)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")

# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 100000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 50000
# Ask if the user wants to continue
st3 = input("Do you want to continue this game? Yes or No")

# Check if the total score reaches the prize pool
prize_amount = score
if (st3 == "Yes"):
        prize_amount = prize
        print("Your final score is:", score)
else:
     print("Your totsl score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize} Rs ") 
     breakpoint()
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
for _ in range(1):  
      for _ in range(1):
          continue
      continue
questions1 = [
    {
        "question": "Q. Which god is also known as 'Gauri Nandan'?" ,
        "options": ["A. Agni" ,"B.Indra" ,"C. Hanuman", "D. Ganesha"],
        "answer": "D"
    },
    # Add more questions here...
]

# Randomly select a question
selected_question = random.choice(questions1)
# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 200000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 50000
# Ask if the user wants to continue
st4 = input("Do you want to continue this game? Yes or No")

# Check if the total score reaches the prize pool
if (st4 == "Yes" ):
    prize_amount = prize
    print("Your final score is:", score)
else:
     print("Your final score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize} Rs")
     total_score = prize
     breakpoint
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
total_score = prize
for _ in range(1):  
      for _ in range(1):
          continue
      continue     
questions2 = [
    {
        "question": "Q. What does not grow on tree according to a popular Hindi saying?" , 
        "options": ["A. Money" , "B. Flowers" , "C. Leaves" , "D. Fruits"],
        "answer": "A"
    },
    # Add more questions here...
]
# Randomly select a question
selected_question = random.choice(questions2)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 300000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 50000
# Ask if the user wants to continue
st5 = input("Do you want to continue this game? Yes or No\n")
# Check if the total score reaches the prize pool
if (st5 == "Yes" ):
        print("Your final score is:", score)     
else:
     print("Your final score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize} Rs")
     total_score = prize
     breakpoint()
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
total_score = prize
for _ in range(1):  
      for _ in range(1):
          continue
      continue
questions3 = [
    {
        "question": "Q. Which city is known as the Pink City of India?"  ,
        "options": ["A. Banglore" , "B. Maysore" , "C. Jaipur" , "D. Kochi" ],
        "answer": "C"
    },
    # Add more questions here...
]

# Randomly select a question
selected_question = random.choice(questions3)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 400000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 50000
# Ask if the user wants to continue
st6 = input("Do you want to continue this game? Yes or No")
# Check if the total score reaches the prize pool
if (st6 == "Yes" ):
    print("Your final score is:", score)
else:
     print("Your final score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize} Rs")
     breakpoint()
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
total_score = prize
for _ in range(1):  
      for _ in range(1):
          continue
      continue
questions4 = [
    {
        "question": "Q. Who wrote India's National Anthem?",
        "options": ["A. Rabindranath Tagore" , "B. Lal Bahadur Shastri" ,  "C. Chetan Bhagat" , "D. RK Narayan" ],
        "answer": "A"
    },
    # Add more questions here...
]

# Randomly select a question
selected_question = random.choice(questions4)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 500000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 50000
# Ask if the user wants to continue
st7 = input("Do you want to continue this game? Yes or No\n")
# Check if the total score reaches the prize pool
if (st7 == "Yes"  ):
        print("Your final score is:", score)
else:
     print("Your final score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize} Rs")
     total_score = prize
     breakpoint()
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
for _ in range(1):  
      for _ in range(1):
          continue
      continue
questions5 = [
    {
        "question":"Q. How many major religions are there in India?" ,
        "options": ["A. 6", "B. 7", "C. 8","D. 9" ],
        "answer": "C"
    },
    # Add more questions here...
]

# Randomly select a question
selected_question = random.choice(questions5)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 1000000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 100000
# Ask if the user wants to continue
st8 = input("Do you want to continue this game? Yes or No\n")
# Check if the total score reaches the prize pool
if (st8 == "Yes" ):
        print("Your final score is:", score)
else:
     print("Your final score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize}Rs")
     total_score = prize
     breakpoint()
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
for _ in range(1):  
      for _ in range(1):
          continue
      continue
questions6 = [
    {
        "question": "Q. When is the National Hindi Diwas celebrated?",
        "options": ["A. 13 September" ,"B. 14 September" ,"C. 14 July" ,"D. 15 August"],
        "answer": "B"
    },
    # Add more questions here...
]
# Randomly select a question
selected_question = random.choice(questions6)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 2000000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    score -= 100000
# Ask if the user wants to continue
st9 = input("Do you want to continue this game? Yes or No\n")
# Check if the total score reaches the prize pool
if (st9 == "Yes" ):
        print("Your final score is:", score)
else:
     print("Your final score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize}Rs")
     total_score = prize
     breakpoint()
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
for _ in range(1):  
      for _ in range(1):
          continue
      continue
questions7 = [
    {
        "question": "Q. Which country is the largest producer of coffee in the world?",
        "options": ["A. Brazil", "B. Colombia", "C. Vietnam", "D. China"],
        "answer": "A"
    },
    # Add more questions here...
]
# Randomly select a question
selected_question = random.choice(questions7)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 13000000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 4500000
# Ask if the user wants to continue
st10 = input("Do you want to continue this game? Yes or No\n")
# Check if the total score reaches the prize pool
if (st10 == "Yes" ):
        print("Your final score is:", score)
else:
     print("Your final score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize} Rs ")
     total_score = prize
     breakpoint()
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
for _ in range(1):  
      for _ in range(1):
          continue
      continue
questions8 = [
    {
        "question":"Q. Where is India Gate located?" ,
        "options": ["A. Punjab", "B. Aagra" ,"C. Mumbai", "D. New Delhi"],
        "answer": "D"
    },
    # Add more questions here...
]
# Randomly select a question
selected_question = random.choice(questions8)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)

# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 12500000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 4900000
# Ask if the user wants to continue
st11 = input("Do you want to continue this game? Yes or No\n")
# Check if the total score reaches the prize pool
if (st11 == "Yes" ):
        print("Your final score is:", score)
else:
     print("Your final score is:", score)
     print(f"Congratulations! You have won the prize pool of {prize} Rs")
     total_score = prize
     breakpoint()
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
for _ in range(1):  
      for _ in range(1):
          continue
      continue
questions9 = [
    {
        "question": "Q. Who wrote Vande Mataram?",
        "options": ["A. Sarat Chandra Chattopadhyay", "B. Rabindranath Tagore" ,"C. Bankim Chandra Chatterjee" ,"D.Ishwar Chandra Vidyasagar"],
        "answer": "C"
    },
    # Add more questions here...
]
# Randomly select a question
selected_question = random.choice(questions9)

# Display the selected question
print(selected_question["question"])
for option in selected_question["options"]:
    print(option)
# Get user's input for the selected question
user_answer = input("Enter your answer (A/B/C/D): ")
# Check if the user's answer is correct
if user_answer == selected_question["answer"]:
    print("Correct!")
    score += 10
    prize += 70000000
else:
    print("Wrong! The correct answer is:", selected_question["answer"])
    score -= 5
    prize -= 8000000
print("Your final score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} Rs")
total_score = prize
print()

# Set the prize pool based on score..
# This this a total scored basesed on game...
# And this is total prize cash based on game....
"""
prize_pool = {
    100: 100000,  # 1 lakh
    200: 200000,  # 2 lakhs
    300: 300000,  # 3 lakhs
    400: 400000,  # 4 lakhs
    500: 500000,  # 5 lakhs
    600: 1000000,  # 10 lakhs
    700: 2000000,  # 20 lakhs
    800: 3000000,  # 30 lakhs
    900: 4000000,  # 40 lakhs
    100: 7000000,  # 7 crores
}
"""
print("Result Are Here:")
print()

print("Your Total score is:", score)
print(f"Congratulations! You have won the prize pool of {prize} crores")
print()
print("Thank You!!")
print("For, playing this game!!")
print()

# Feedback!!!

FROM_EMAIL = input("Do you like this (KBC) game, you can write your email id!!\n")
MESSAGE = input("Feedback!!-\n ")
print("Thank You , see you again!!!")

