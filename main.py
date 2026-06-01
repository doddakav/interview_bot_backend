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
    Generate the questions on

    Topic: {topic}
    Difficulty: {level}
    Question Types: {', '.join(ways)}

    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
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