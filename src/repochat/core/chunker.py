# src/repochat/core/chunker.py

def split_documents(documents: list[str], chunk_size: int = 1000) -> list[str]:
    """
    Split each document string into chunks of a given size.

    Args:
        documents: List of document text strings.
        chunk_size: Maximum number of characters per chunk.

    Returns:
        List of text chunks.
    """
    chunks = []
    for doc in documents:
        for i in range(0, len(doc), chunk_size):
            chunks.append(doc[i:i + chunk_size])
    return chunks
