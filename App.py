import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def get_answer(prompt: str) -> str:
    """
    Sends a prompt to Gemini Flash Lite model
    and returns the generated response text.
    """

    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=prompt
    )

    return response.text


# Optional: run directly for terminal testing
if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (type 'exit' to quit): ")
        if q.lower() == "exit":
            break

        answer = get_answer(q)
        print("\n🤖 Answer:")
        print(answer)
