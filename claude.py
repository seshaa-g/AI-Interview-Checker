import os
from anthropic import Anthropic

# Initialize Claude client
client = Anthropic(api_key="YOUR_API_KEY")  # <-- replace with your key

# Take inputs from terminal
actual_answer = input("Enter Actual Answer:\n")
transcribed_answer = input("\nEnter Transcribed Answer:\n")

# Prompt Claude
prompt = f"""
Compare the following two answers:

Actual Answer:
{actual_answer}

Transcribed Answer:
{transcribed_answer}

Give only a similarity/accuracy score between 0 and 100 (100 = perfectly accurate).
Just return the number, no explanation.
"""

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=50,
    messages=[{"role": "user", "content": prompt}]
)

print("\nClaude Accuracy Score:", response.content[0].text.strip())
