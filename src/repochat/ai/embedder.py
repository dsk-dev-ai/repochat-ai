from langchain_community.embeddings import OllamaEmbeddings


def create_embeddings():
    return OllamaEmbeddings(
        model="phi",
        base_url="http://localhost:11434"
    )