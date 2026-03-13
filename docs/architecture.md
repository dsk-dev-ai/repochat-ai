# Full Project Structure 

repochat-ai/
│
├── src/
│   └── repochat/
│       ├── __init__.py
│       ├── version.py
│       ├── cli.py
│       │
│       ├── core/
│       │   ├── __init__.py
│       │   ├── clone_repo.py
│       │   ├── file_loader.py
│       │   ├── chunker.py
│       │   └── config.py
│       │
│       ├── ai/
│       │   ├── __init__.py
│       │   ├── embedder.py
│       │   ├── vector_store.py
│       │   └── chat_engine.py
│       │
│       └── utils/
│           ├── __init__.py
│           ├── logger.py
│           └── helpers.py
│
├── tests/
│   └── test_chat.py
│
├── examples/
│   └── demo.py
│
├── docs/
│   └── architecture.md
│
├── requirements.txt
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
