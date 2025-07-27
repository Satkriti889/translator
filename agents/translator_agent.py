# agents/translator_agent.py
import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core import exceptions # Import for specific error handling

# Load environment variables from .env file
load_dotenv()

# Get API key and ensure it exists
API_KEY = os.getenv("satkriti_api")
if not API_KEY:
    raise ValueError("API_KEY not found in environment variables or .env file. Please set it.")

# Configure the generative AI model with the API key
genai.configure(api_key=API_KEY)

def translate_english_to_nepali(text: str) -> str:
    """
    Translates an English sentence to Nepali using a stable Gemini model.

    Args:
        text (str): The English sentence to translate.

    Returns:
        str: The translated Nepali sentence, or an error message if translation fails.
    """
    # Changed model to gemini-2.5-flash-preview-05-20 for wider availability and stability
    model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
    
    # --- MODIFIED PROMPT HERE ---
    # Instruct the model to provide ONLY the Nepali translation.
    prompt = f"Translate the following English sentence into Nepali. Provide only the Nepali translation, without any additional explanations or formatting:\n\n{text}"
    
    try:
        # Generate content using the model
        response = model.generate_content(prompt)
        # Return the translated text, stripping any leading/trailing whitespace
        return response.text.strip()
    except exceptions.GoogleAPIError as e:
        # Handle specific Google API errors (e.g., quota issues, invalid requests)
        print(f"An API error occurred during translation: {e}")
        return "Translation failed due to an API error."
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred during translation: {e}")
        return "Translation failed due to an unexpected error."
