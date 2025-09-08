import os
import requests
import json
import re
import string
import textwrap
from dotenv import load_dotenv

load_dotenv()

def api_call():
    # Letting the user choose their own topic
    topic = input("Choose the topic: ")
    API_KEY = os.getenv("QUIZ_GAME_GOOGLE_API_KEY")
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }
    data = {
    "contents": [
        {
            "parts": [
                {
                    "text": textwrap.dedent(f"""
    Give me:
    - 5 easy
    - 5 medium
    - 5 hard MCQs

    Topic: {topic}

    Format the output strictly in JSON with keys:
    - "easy"
    - "medium"
    - "hard"
""")
                }
            ]
        }
    ]
}

    return url, headers, data




def get_question():
     url, headers, data = api_call()

     response = requests.post(url, headers=headers, json=data, timeout=30)

     result = response.json()
    
     raw_text = result['candidates'][0]['content']['parts'][0]['text']
     
     matches = re.findall(r"\{.*\}", raw_text, re.DOTALL)

     if matches:
        clean_text = max(matches, key=len)  # take only the JSON part
        questions_data = json.loads(clean_text)
     else:
        raise ValueError("No JSON found in API response")
        
     return questions_data


def ask_question(question, level_name):
    # Printing difficulty level
     print(f"\n=== {level_name.upper()} QUESTIONS ===")
     
    # Printing Question
     print("Q:", question['question'])

    # Print options with letters
     for i, option in enumerate(question["options"]):
        letter = string.ascii_lowercase[i]
        print(f"{letter}. {option}")
    
    # Convert the correct answer text into its letter
     for i, option in enumerate(question["options"]):
        if option == question["answer"]:
            correct_letter = string.ascii_lowercase[i]
            break
        
     user_input = ""
     # Preventing user from mistyping
     while user_input not in ['a', 'b', 'c', 'd']:
         user_input = input("\nYour answer: ").strip().lower()
         if user_input not in ['a', 'b', 'c', 'd']:
             print("\nInvalid input!")


    
     if user_input == correct_letter :
        print("\nCorrect")
        return True
     else:
        print("\nIncorrect")
        print("\nAnswer:", question["answer"])
        return False


def play_quiz(quiz):

    score = 0

     # Levels in order
    levels = [("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")]
    
    for key, name in levels:
        # Getting questions using difficulty level
        if key not in quiz:
            print(f"⚠️ No questions found for {key}")
            continue
        # Getting questions one by one
        for question in quiz[key]:

            if not ask_question(question, name):
                print("\nGame Over! 😢")
                print (f"Score: {score}/15") # Stop if wrong
                return
            score += 1
    
        

    print("\n🎉 Congratulations! You completed all levels!")


def main():
    quiz = get_question()
    play_quiz(quiz)
    
if __name__ == "__main__":
    main()
