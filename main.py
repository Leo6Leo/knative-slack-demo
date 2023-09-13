from fastapi import FastAPI
import httpx

app = FastAPI()

SLACK_URL = "https://hooks.slack.com/services/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"

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
