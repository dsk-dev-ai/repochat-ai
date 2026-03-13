# src/repochat/cli.py

import typer
from repochat.core.clone_repo import clone_repository
from repochat.core.file_loader import load_code_files
from repochat.core.chunker import split_documents
from repochat.ai.embedder import create_embeddings
from repochat.ai.vector_store import create_vector_db
from repochat.ai.chat_engine import create_chat_engine

app = typer.Typer(help="RepoChat: Chat with any GitHub repository using local AI")

@app.command()
def chat(repo_url: str):
    """
    Clone a GitHub repo and chat with its codebase.
    
    Example:
        repochat chat https://github.com/vercel/next.js
    """
    # 1. Clone repository
    repo_path = clone_repository(repo_url)
    
    # 2. Load code files into a list of documents
    docs = load_code_files(repo_path)
    typer.secho(f"Loaded {len(docs)} code files.", fg=typer.colors.GREEN)
    
    # 3. Split documents into chunks
    chunks = split_documents(docs)
    typer.secho(f"Split into {len(chunks)} chunks.", fg=typer.colors.GREEN)
    
    # 4. Create embeddings and vector DB
    embeddings = create_embeddings()
    vector_db = create_vector_db(chunks, embeddings)
    typer.secho("Vector database created.", fg=typer.colors.GREEN)
    
    # 5. Create chat engine and start interactive chat
    engine = create_chat_engine(vector_db)
    typer.secho("\nRepoChat is ready! Ask a question (type 'exit' to quit):\n", fg=typer.colors.BLUE)
    
    while True:
        query = typer.prompt(">>>")
        if query.lower() in ("exit", "quit"):
            typer.secho("Exiting RepoChat. Goodbye!", fg=typer.colors.YELLOW)
            break
        answer = engine.run(query)
        typer.echo(answer)

if __name__ == "__main__":
    app()
