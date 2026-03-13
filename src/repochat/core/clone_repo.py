# src/repochat/core/clone_repo.py

import os
import git
from .config import REPO_STORAGE

def clone_repository(repo_url: str) -> str:
    """
    Clone a GitHub repository URL into a local folder.
    If already cloned, reuse the existing copy.

    Args:
        repo_url: URL of the GitHub repo (HTTPS or SSH).
    
    Returns:
        Path to the cloned repository directory.
    """
    os.makedirs(REPO_STORAGE, exist_ok=True)
    repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
    repo_path = os.path.join(REPO_STORAGE, repo_name)

    if os.path.exists(repo_path):
        print(f"Repository already cloned at {repo_path}.")
        return repo_path

    print(f"Cloning {repo_url} into {repo_path} ...")
    git.Repo.clone_from(repo_url, repo_path)
    print("Clone completed.")
    return repo_path
