
class VectorStore:
    """
    A simple in-memory cache for storing and retrieving translations.
    This acts as a mock vector store for demonstration purposes,
    performing exact match lookups instead of semantic similarity.
    """
    def __init__(self):
        # The cache stores original_text -> translated_text mappings
        self._cache = {}

    def add_translation(self, original_text: str, translated_text: str):
        
        self._cache[original_text] = translated_text

    def search_similar(self, text: str, k: int = 3):
        
        if text in self._cache:
            
            return [(text, self._cache[text])] 
        return []

