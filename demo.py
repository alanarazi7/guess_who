from openai_calls import ask_openai

# Define 5 characters with random names and genders
characters = [
    {"name": "Alex", "gender": "Male"},
    {"name": "Taylor", "gender": "Female"},
    {"name": "Jordan", "gender": "Male"},
    {"name": "Morgan", "gender": "Female"},
    {"name": "Casey", "gender": "Male"}
]


# Start the game
print("Welcome to the AI-Powered 'Guess Who' Game!")
print("Characters:")
for i, char in enumerate(characters):
    print(f"{i+1}. Name: {char['name']}, Gender: {char['gender']}")

print("\nThink of a character from the list above, and the AI will try to guess it!")

# Turn 1
ai_question_1 = "Is your character male or female?"
print(f"AI: {ai_question_1}")
user_answer_1 = input("You: ")

# Use OpenAI to simulate a second question based on the user answer
ai_prompt_2 = f"The user said their character is {user_answer_1}. Ask a second question to guess their character."
ai_question_2 = ask_openai(ai_prompt_2)
print(f"AI: {ai_question_2}")
user_answer_2 = input("You: ")

# Simulate AI guess based on the answers
ai_prompt_guess = f"Based on the answers: 1) {user_answer_1}, 2) {user_answer_2}, guess the character from the following list: {characters}."
ai_guess = ask_openai(ai_prompt_guess)
print(f"AI: I guess your character is {ai_guess}!")
