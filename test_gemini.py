import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Step A: Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY in environment variables")

# Step B: Load config JSON (optional)
with open("config.json", "r") as f:
    config = json.load(f)

# Step C: Configure the API client
genai.configure(api_key=API_KEY)

# Step D: Initialize the model (use a valid model name from your list)
model = genai.GenerativeModel("models/gemini-1.5-flash")


# Step E: Prepare a prompt
prompt = "Write a professional email marketing message promoting a summer sale."

# Step F: Generate content from the model
response = model.generate_content(prompt)

# Step G: Print the generated text
print("Generated Email Content:\n", response.text)
