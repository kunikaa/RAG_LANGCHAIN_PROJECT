import os
from dotenv import load_dotenv
from google import genai

load_dotenv()   # 🔥 testing ke liye MOST IMPORTANT

api_key = os.getenv("GOOGLE_API_KEY")
print("API KEY FOUND:", bool(api_key))  # sanity check

client = genai.Client(api_key=api_key)

models = client.models.list()
for m in models:
    print(m.name)
