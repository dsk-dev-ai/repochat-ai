# examples/demo.py

import subprocess

def main():
    repo_url = "https://github.com/vercel/next.js"
    subprocess.run(["repochat", "chat", repo_url])

if __name__ == "__main__":
    main()
