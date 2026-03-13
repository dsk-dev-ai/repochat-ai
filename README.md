# RepoChat AI

Chat with any GitHub repository using local AI.  
Understand codebases instantly with natural language.

**RepoChat AI** lets you ask questions about a repo’s source code. It works offline using [Ollama](https://ollama.com/) and [LangChain](https://docs.langchain.com/) under the hood.

⭐ Star this repo if it helps you!

## Demo

![RepoChat Demo](./docs/demo.gif)

In this example, we run RepoChat on the Next.js repository and ask about routing:

```bash
$ repochat chat https://github.com/vercel/next.js
Cloning repository...
Loaded 80 files
Split into 600 chunks
Vector database created.
RepoChat is ready! Ask a question (type 'exit' to quit):

>>> How does routing work in Next.js?
Next.js uses a file-system based router. ... (AI-generated answer) ...
```

## Features

- Interactive CLI chat with any GitHub repo
- Uses local open-source LLMs via Ollama
- Splits large codebases into searchable chunks
- Generates responses by retrieving context from code

## Installation

```bash
pip install repochat-ai
```

(Requires Python 3.8+ and Ollama installed and running locally.)

## Usage

```bash
repochat chat https://github.com/username/repo.git
```

Then ask natural language questions about the code.

## Development

To run locally from source:

```bash
git clone https://github.com/USERNAME/repochat-ai.git
cd repochat-ai
pip install -e .   # install dependencies
repochat chat https://github.com/vercel/next.js
```

## Contributing

Contributions welcome! Please open issues or pull requests. This project follows standard Python packaging guidelines.

## License

MIT License. See LICENSE for details.

## Creating a Demo GIF

A demo GIF significantly increases interest. Steps:

1. **Install Tools:**  
   - On Windows: [ScreenToGif](https://www.screentogif.com/) or OBS Studio.  
   - On macOS: [Kap](https://getkap.co/) or QuickTime + ffmpeg.  
   - On Linux: `gtk-recordmydesktop` or `Peek`.

2. **Record Steps:**  
   - Show installing (if fresh).  
   - Run `repochat chat <example-repo>`.  
   - Type a sample question.  
   - Copy the answer from terminal.

3. **Edit GIF:**  
   - Crop to focus on terminal.  
   - Add slight delays between lines.  
   - Keep it short (<15s).

4. **Save:** Put the GIF at `docs/demo.gif` in your repo.

Adding `docs/demo.gif` in README makes the project visually appealing, attracting more stars.

## Git Commands (Push to GitHub)

Once everything is ready, you can push to GitHub:

```bash
git init
git add .
git commit -m "Initial RepoChat AI release with full code"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/repochat-ai.git
git push -u origin main
```

Replace YOUR_USERNAME with your GitHub username.
This creates a new repository and pushes your code. For future changes, just git add, commit, and push.
