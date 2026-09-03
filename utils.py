import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)


def get_ai_response(prompt: str) -> str:
    """Sends a prompt to Gemini 3.5 Flash and returns the text response."""
    if not api_key:
        return "Error: GEMINI_API_KEY is missing from your environment variables or .env file."
    
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"