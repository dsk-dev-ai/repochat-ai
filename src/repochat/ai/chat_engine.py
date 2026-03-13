from langchain_community.llms import Ollama
from langchain_classic.chains import RetrievalQA


def create_chat_engine(vector_db):

    llm = Ollama(
        model="phi",
        base_url="http://localhost:11434"
    )

    retriever = vector_db.as_retriever()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa