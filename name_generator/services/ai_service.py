# name_generator/services/ai_service.py
import json
from openai import OpenAI
import os

# Load API key and URL from environment variables
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_URL = os.getenv("DEEPSEEK_URL")

def generate_baby_names(father_name, mother_name, siblings, country, language, name_style, religion, gender):
    system_content = """You are an expert in baby name suggestions. Your task is to suggest three names based on the provided details.
    For each name, include:
    - The name itself
    - A brief meaning of the name
    - Popularity or notable figures associated with the name

    Return the results in STRICT JSON format as follows:
    {
        "name1": {"name": "Name 1", "meaning": "Meaning of Name 1", "details": "Details about Name 1"},
        "name2": {"name": "Name 2", "meaning": "Meaning of Name 2", "details": "Details about Name 2"},
        "name3": {"name": "Name 3", "meaning": "Meaning of Name 3", "details": "Details about Name 3"}
    }

    Ensure that the response contains ONLY JSON and no additional text."""

    user_content = f"""
    Father's Name: {father_name}
    Mother's Name: {mother_name}
    Siblings' Names: {siblings}
    Country: {country}
    Language: {language}
    Preferred Style: {name_style}
    Religion: {religion}
    Baby's Gender: {gender}
    """

    try:
        client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_URL)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            stream=False
        )
        response_content = response.choices[0].message.content

        # Log the raw response for debugging
        print("Raw API Response:", response_content)

        # Parse JSON response
        try:
            return json.loads(response_content)
        except json.JSONDecodeError as e:
            if not response_content.strip():  # Check if response is empty
                return "Error: The API returned an empty response."
            return f"Error: Failed to parse AI response - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"