from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document


def create_vector_db(chunks, embeddings):

    # Convert text chunks to Document objects
    docs = [Document(page_content=chunk) for chunk in chunks]

    vector_db = Chroma.from_documents(
        docs,
        embeddings,
        collection_name="repochat"
    )

    return vector_db