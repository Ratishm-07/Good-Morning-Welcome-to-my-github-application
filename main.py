# main.py

import os
import git
from datetime import datetime

# Configuration
REPO_URL = "https://github.com/yourusername/your-cloud-repo.git"
LOCAL_REPO_DIR = "cloud_project_repo"
COMMIT_MESSAGE = f"Automated update - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def clone_or_pull_repo():
    if not os.path.exists(LOCAL_REPO_DIR):
        print(f"Cloning repository from {REPO_URL}...")
        repo = git.Repo.clone_from(REPO_URL, LOCAL_REPO_DIR)
    else:
        print("Repository already exists. Pulling latest changes...")
        repo = git.Repo(LOCAL_REPO_DIR)
        origin = repo.remotes.origin
        origin.pull()
    return repo

def make_changes_and_commit(repo):
    dummy_file = os.path.join(LOCAL_REPO_DIR, "update_log.txt")
    print("Making changes to update_log.txt...")
    with open(dummy_file, "a") as f:
        f.write(f"Updated at {datetime.now()}\n")
    
    repo.git.add(A=True)
    
    if repo.is_dirty():
        print("Changes detected. Committing...")
        repo.index.commit(COMMIT_MESSAGE)
    else:
        print("No changes to commit.")

def push_changes(repo):
    print("Pushing changes to remote...")
    origin = repo.remotes.origin
    origin.push()
    print("Push complete.")

def main():
    print("=== Cloud Git Manager ===")
    repo = clone_or_pull_repo()
    make_changes_and_commit(repo)
    push_changes(repo)

if __name__ == "__main__":
    main()
