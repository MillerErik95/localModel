import os
from typing import List, Dict
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

TEST_MODE = True  # Change to False for real API calls

def generate_response(messages: List[Dict]) -> str:
    """Call Claude to get a response"""
    if TEST_MODE:
        print("🧪 TEST_MODE is enabled. Returning mock response.")
        return "🧪 Response in TEST MODE"

    print("⚙️ Preparing request for Claude API...")

    system = next((msg["content"] for msg in messages if msg["role"] == "system"), None)
    anthropic_messages = [
        {"role": msg["role"] if msg["role"] != "system" else "user", "content": msg["content"]}
        for msg in messages if msg["role"] != "system"
    ]

    print("📡 Sending request to Claude...")
    response = client.messages.create(
        model="claude-3-5-haiku-latest",
        system=system,
        messages=anthropic_messages,
        max_tokens=1024
    )

    print("✅ Received response from Claude.")
    return response.content[0].text