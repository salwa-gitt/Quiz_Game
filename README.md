# 🧠 AI Quiz Game (Python + Gemini API)

An interactive console-based quiz game that generates multiple-choice questions dynamically using Google's Gemini API. The game includes different difficulty levels and tests users progressively from easy to hard questions.

---

## 🚀 Features

- 🤖 AI-generated MCQs using Gemini API
- 📊 Three difficulty levels (Easy, Medium, Hard)
- 🎯 Instant answer validation
- 🧩 Dynamic question parsing from JSON
- 🛑 Game ends on incorrect answer
- 🧠 Score tracking system
- 🔄 Fully interactive CLI experience

---

## 🛠️ Tech Stack

- Python
- Google Gemini API (Generative AI)
- Requests library
- JSON handling
- Regex parsing
- Environment variables (`dotenv`)

---

## 🧠 How It Works

1. User selects a topic
2. Program sends request to Gemini API
3. AI generates MCQs in JSON format
4. Questions are parsed and organized by difficulty
5. User answers each question step-by-step
6. Game ends on wrong answer or completion

---

## 📌 Game Flow

```
Easy → Medium → Hard
      ↓
Correct Answer → Next Question
Wrong Answer → Game Over
```

---

## 💡 Example Usage

```
Choose the topic: Python

=== EASY QUESTIONS ===
Q: What is a variable in Python?
a. A function
b. A storage container
c. A loop
d. A library

Your answer: b
Correct
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
QUIZ_GAME_GOOGLE_API_KEY=your_api_key_here
```

---

## 📚 Concepts Used

- REST API integration
- AI-generated content handling
- JSON parsing
- Regex extraction
- Loops & conditionals
- Modular programming
- CLI design

---

## 🔮 Future Improvements

- Add timer-based questions
- Add score leaderboard
- Add difficulty selection menu
- Add GUI version (Tkinter / Web app)
- Save user progress
- Add multiple AI models support

---

## 🎯 Learning Outcome

This project demonstrates:
- Real-world AI API integration
- Dynamic data handling from external sources
- Structured game logic design
- Clean modular Python architecture

---

## 👨‍💻 Author

Built by Salwa
