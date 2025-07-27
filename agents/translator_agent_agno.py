from agents.translator_agent import translate_english_to_nepali

class TranslatorAgentAGNO:
    """
    A simple agent class to encapsulate the translation functionality.
    This class is used by main.py to interact with the translator.
    """
    def run(self, input_text: str) -> str:
        """
        Executes the English to Nepali translation for the given text.

        Args:
            input_text (str): The English sentence to be translated.

        Returns:
            str: The translated Nepali sentence.
        """
        return translate_english_to_nepali(input_text)
