# tests/test_chat.py

import os
import tempfile
import pytest
from repochat.core.clone_repo import clone_repository
from repochat.core.file_loader import load_code_files
from repochat.core.chunker import split_documents
from repochat.ai.embedder import create_embeddings

def test_split_documents():
    docs = ["abcde"]
    chunks = split_documents(docs, chunk_size=2)
    assert chunks == ["ab", "cd", "e"]

def test_load_code_files(tmp_path):
    # Create a temporary Python file
    file = tmp_path / "test.py"
    content = "print('hello')\n"
    file.write_text(content)
    docs = load_code_files(str(tmp_path))
    assert docs == [content]

def test_clone_repository(tmp_path):
    # Simulate cloning by creating a fake git repo structure
    repo_path = tmp_path / "repos"
    repo_name = "dummy-repo"
    os.makedirs(repo_path / repo_name, exist_ok=True)
    # Create dummy file
    file = repo_path / repo_name / "file.txt"
    file.write_text("data")
    # Monkeypatch git.Repo.clone_from to just return path
    from repochat.core.clone_repo import git as _git_module
    class DummyRepo:
        @staticmethod
        def clone_from(url, path):
            return None
    orig_git = _git_module
    _git_module.Repo = DummyRepo
    
    result = clone_repository(f"http://example.com/{repo_name}.git")
    assert result.endswith(repo_name)

    # Restore git module (not strictly needed in real test)
    _git_module.Repo = orig_git.Repo

def test_version():
    import repochat
    assert hasattr(repochat, '__version__')
