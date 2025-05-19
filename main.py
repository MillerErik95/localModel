import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("OPENAI_API_KEY:", api_key)