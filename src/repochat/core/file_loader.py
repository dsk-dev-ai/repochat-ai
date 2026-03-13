# src/repochat/core/file_loader.py

import os
from .config import SUPPORTED_EXTENSIONS

def load_code_files(repo_path: str) -> list[str]:
    """
    Recursively load all code files from a cloned repository path.

    Args:
        repo_path: Local filesystem path of the repository.

    Returns:
        A list of text contents of all supported files.
    """
    documents = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                    documents.append(text)
                except Exception:
                    # Skip unreadable files
                    continue
    return documents
