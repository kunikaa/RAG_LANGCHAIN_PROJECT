import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    while True:
        q = input("\nAsk a question (or type exit): ")
        if q.lower() == "exit":
            break

        response = client.models.generate_content(
            model="models/gemini-flash-lite-latest",
            contents=q
        )

        print("\n🤖 Answer:")
        print(response.text)

if __name__ == "__main__":
    main()
