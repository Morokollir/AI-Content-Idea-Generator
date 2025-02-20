import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content_ideas(keyword):
    prompt = f"Generate five creative content ideas for the topic: {keyword}. Include blog posts, video ideas, and social media post suggestions."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative content strategist."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    keyword = input("Enter a keyword or topic: ")
    ideas = generate_content_ideas(keyword)
    print("\nGenerated Content Ideas:\n", ideas)
