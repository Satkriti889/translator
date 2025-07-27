import faiss
import numpy as np

class SimpleVectorStore:
    """
    A simple in-memory vector store using FAISS for efficient similarity search.
    Stores text associated with its embedding vector.
    """
    def __init__(self, dim: int = 1536):
        """
        Initializes the vector store.

        Args:
            dim (int): The dimension of the vectors (default for text-embedding-3-small is 1536).
        """
        self.index = faiss.IndexFlatL2(dim) # L2 distance for similarity
        self.texts = [] # Stores the corresponding original texts

    def add(self, vector: list[float], text: str):
        """
        Adds a vector and its associated text to the store.

        Args:
            vector (list[float]): The embedding vector to add.
            text (str): The text associated with the vector.
        """
        # Convert vector to numpy array with float32 type for FAISS
        self.index.add(np.array([vector], dtype=np.float32))
        self.texts.append(text)

    def search(self, vector: list[float], k: int = 3) -> list[str]:
        """
        Searches for the k most similar texts to the given vector.

        Args:
            vector (list[float]): The query embedding vector.
            k (int): The number of nearest neighbors to retrieve.

        Returns:
            list[str]: A list of texts similar to the query vector.
        """
        # Ensure the vector is not empty (e.g., if embedding failed)
        if not vector:
            return []

        # Search the FAISS index
        D, I = self.index.search(np.array([vector], dtype=np.float32), k)
        # Retrieve the texts corresponding to the indices, ensuring they are valid
        return [self.texts[i] for i in I[0] if i < len(self.texts)]
