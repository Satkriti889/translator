
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class TranslatorAgent:
   
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set. Please create a .env file and add your Gemini API key.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-2.5-pro') 

    def _translate(self, text: str, target_language: str) -> str:
        
        prompt = f"Only give the exact translation of the following text to {target_language}, without any explanation or extra text:\n\n{text}"
        try:
            response = self.model.generate_content(prompt)
            
            if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
                return response.candidates[0].content.parts[0].text.strip()
            else:
                return ""
        except Exception as e:
            
            print(f"Error during translation with Gemini API: {e}")
            return ""

    def translate_english_to_nepali(self, text: str) -> str:
        
        return self._translate(text, "Nepali")

    def translate_nepali_to_english(self, text: str) -> str:
        
        return self._translate(text, "English")

