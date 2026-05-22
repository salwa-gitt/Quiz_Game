# AI Quiz Game (Python + Gemini API)

An interactive terminal-based quiz game powered by Google’s Gemini API. The game dynamically generates multiple-choice questions based on a user-selected topic and challenges the player across three difficulty levels: Easy, Medium, and Hard.

## Features

- AI-generated MCQs using Gemini API
- User-defined quiz topic
- Three difficulty levels:
  - Easy (5 questions)
  - Medium (5 questions)
  - Hard (5 questions)
- Interactive command-line gameplay
- Answer validation with instant feedback
- Score tracking system
- Game over on first wrong answer (challenge mode)

## Tech Stack

- Python 3
- Google Generative Language API (Gemini)
- Requests library
- Regex (for response parsing)
- dotenv (for API key security)

## Project Structure

```bash
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-quiz-game.git
cd ai-quiz-game
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API Key
Create a `.env` file and add your Gemini API key:

```env
QUIZ_GAME_GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the game
```bash
python main.py
```

## How It Works

1. User enters a topic (e.g., Python, AI, History)
2. Program sends a prompt to Gemini API
3. AI returns structured MCQs in JSON format
4. Game parses questions into difficulty levels
5. Player answers questions in sequence
6. One wrong answer ends the game

## Example Gameplay

```
Choose the topic: Python

=== EASY QUESTIONS ===
Q: What is Python?
a. A snake
b. A programming language
c. A database
d. A game

Your answer: b
Correct
```

## Key Functions

### `api_call()`
Builds and sends request to Gemini API with prompt for MCQs.

### `get_question()`
Fetches and cleans API response into structured JSON.

### `ask_question(question, level_name)`
Handles question display, user input, and answer validation.

### `play_quiz(quiz)`
Controls game flow across difficulty levels and score tracking.

## Concepts Demonstrated

- API integration (REST)
- JSON parsing
- Regex data extraction
- Environment variables (.env security)
- Modular function design
- CLI-based game logic

## Future Improvements

- Add multiple lives instead of instant game over
- Add timer per question
- Store high scores locally or in database
- Add GUI version (Tkinter or web app)
- Add categories + difficulty scaling system
- Multiplayer mode

## Learning Outcome

This project demonstrates how AI APIs can be integrated into Python applications to build dynamic, interactive systems beyond static datasets.

## Author

Built by Salwa
