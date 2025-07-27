# Add this to any file temporarily
import os
from dotenv import load_dotenv

load_dotenv()
print("OPENAI API KEY:", os.getenv("OPENAI_API_KEY"))
