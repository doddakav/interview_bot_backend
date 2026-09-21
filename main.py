from fastapi import FastAPI, Request
from openai import OpenAI
import os
app = FastAPI()

client = OpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url")
)
@app.get("/")
def home():
    return {
        "message": "AI Interview Bot API Running"
    }

@app.post("/generate-question")
async def generate_question(request: Request):

    data = await request.json()

    topic = data.get("topic")
    level = data.get("level")
    ways = data.get("ways")

    prompt = f"""
You are an expert technical interviewer.

Create a professional interview question set using these parameters:

Topic: {topic}
Difficulty: {level}
Question Types: {', '.join(ways)}

Question type guidelines:
- Conceptual: Ask about important concepts, definitions, principles, and how they work.
- Coding: Give a programming problem that requires the candidate to write or explain code.
- Scenario-Based: Present a realistic technical situation and ask how the candidate would solve it.
- MCQ: Provide one question with exactly 4 options and identify the correct answer.
- Behavioral: Ask about the candidate's experience, problem-solving approach, teamwork, or decision-making.

Requirements:
- Generate exactly 5 questions.
- Use only the requested question types.
- Questions must be relevant to the specified topic.
- Match the specified difficulty.
- Avoid duplicate questions.
- Avoid questions that can be answered with only yes/no.
- Make questions progressively challenging when possible.
- Keep the wording clear and professional.
- Do not provide explanations or answers unless required by the question type.

Return the result in this format:

1. [Question]
2. [Question]
3. [Question]
4. [Question]
5. [Question]
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "questions": response.choices[0].message.content
    }