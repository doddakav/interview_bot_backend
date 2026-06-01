# AI Interview Bot Backend

## Overview

This is the FastAPI backend for the AI Interview Bot. It generates interview questions based on topic, difficulty level, and question type using the Groq LLM API.

## Features

* Generate AI-powered interview questions
* Support for multiple difficulty levels
* Support for multiple question types
* FastAPI REST API
* Deployable on Render

## Tech Stack

* Python
* FastAPI
* Uvicorn
* OpenAI SDK
* Groq API

## Project Structure

backend/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

## Installation

Clone the repository:

git clone https://github.com/doddakav/interview_bot_backend.git

Move to project directory:

cd interview_bot_backend

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create environment variables in Render:

GROQ_API_KEY=your_api_key

## Run Locally

uvicorn main:app --reload

API URL:

http://127.0.0.1:8000

## Endpoints

### Home

GET /

Response:

{
"message": "AI Interview Bot API Running"
}

### Generate Questions

POST /generate-question

Request:

{
"topic": "Python",
"level": "Easy",
"ways": ["MCQ", "Theory"]
}

Response:

{
"questions": "Generated interview questions..."
}

## Deployment

Platform: Render

Build Command:

pip install -r requirements.txt

Start Command:

uvicorn main:app --host 0.0.0.0 --port $PORT
live working url: https://interviewbotfrontend.streamlit.app/
## Author

Vinod Doddaka
