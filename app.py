from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

client = genai.Client()

no_recipes = input("No of recipes (for example, 5): ")
ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used."

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)