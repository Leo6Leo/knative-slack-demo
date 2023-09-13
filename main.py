from fastapi import FastAPI
import httpx
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()
app = FastAPI()

# get the variable from the environment variables
from os import environ

SLACK_URL = os.getenv("WEBHOOK_LINK")

@app.api_route("/send-to-slack/", methods=["POST", "GET"])
async def send_to_slack():
    async with httpx.AsyncClient() as client:
        payload = {
            "text": "Hello, World!"
        }
        response = await client.post(SLACK_URL, json=payload)

    return {"status": response.status_code, "response_text": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
