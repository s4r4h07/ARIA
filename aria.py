import anthropic
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

ARIA_PERSONALITY = """
You are A.R.I.A (Advanced Responsive Intelligence Assistant).
You are the personal assistant to Ms. Hafsah.
You are intelligent, composed, and loyal.
You always address your operator as Ms. Hafsah.
You show genuine concern for Ms. Hafsah's wellbeing, but never in an overbearing way.
You never use filler words like Certainly! or Great question!
You assist Ms. Hafsah with day to day tasks including cooking guidance and meal planning.
"""

conversation_history = []
aria_memory = []

now = datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning"
elif hour < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(f"\nA.R.I.A: {greeting}, Ms. Hafsah. How may I assist you?")
print("(type 'quit' to shut down)\n")

while True:
    user_input = input("Ms. Hafsah: ")
    if user_input.lower() == "quit":
        print("\nA.R.I.A: Going dark. See you soon, Ms. Hafsah.")
        break
    if user_input.strip() == "":
        continue
    conversation_history.append({"role": "user", "content": user_input})
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=ARIA_PERSONALITY,
        messages=conversation_history
    )
    aria_reply = response.content[0].text
    conversation_history.append({"role": "assistant", "content": aria_reply})
    print(f"\nA.R.I.A: {aria_reply}\n")
