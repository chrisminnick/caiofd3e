# Simple Survey Analyzer
  
print("Welcome to the Super Quick Survey!")
print("----------------------------------")
  
# Store the survey questions in a list
questions = [
    "What's your name? ",
    "How old are you? ",
    "What's your favorite programming language so far? "
]
  
# Create an empty list to store the answers
answers = []
  
# Loop through the questions
for question in questions:
  
    # Get the answer to the next question
    answer = input(question)
  
    # Add the answer to the answers list
    answers.append(answer)
  
# Unpack the answers into variables
name = answers[0]
age = int (answers[1])
language = answers[2]
  
# Respond based on their input
# The \n in the string prints a blank line
print(f"\nThanks, {name}! Here's your survey summary:\n")
  
print(f"You are {age} years old.")
  
# Add some conditional feedback
# about their age
if age < 18:
    print("You're off to an early start — awesome!")
elif age > 60:
    print("Proving it's never too late to learn!")
else:
    print("Perfect time in life to be learning something new!")
  
print(f"\nYou enjoy coding in {language}.")
  
# Add some conditional feedback about
# their programming language choice
if language.lower() == "python":
    print("Great choice — Python is beginner-friendly and powerful!")
elif language.lower() == "javascript":
    print("Nice! JavaScript makes the web come alive.")
else:
    print(f"{language}? Very cool. Every language has its own superpower.")
  
print("\nThanks for taking the survey!")
