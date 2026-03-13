from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="repochat-ai",
    version="0.1.0",
    author="Darshan Kachare",
    description="Chat with any GitHub repository using local AI (Ollama)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain",
        "chromadb",
        "ollama",
        "gitpython",
        "typer",
        "rich",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "repochat=repochat.cli:app"
        ]
    },
)