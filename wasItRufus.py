import os
import subprocess
from datetime import datetime, timezone
import argparse

def git_status(git_dir):
    # First check if the provided path exist and is a directory
    if not os.path.isdir(git_dir):
        raise FileNotFoundError("The Provided Path does not exist or is not a directory")

    os.chdir(git_dir)
    # Check if the Directory is a git Directory
    try:
        branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], stdout=subprocess.PIPE, check=True).stdout.strip().decode()
    except subprocess.CalledProcessError as e:
        raise ValueError("The provided git_dir is not a git repository") from e
    
    # Grabs the necessary data using git commands
    modified = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE).stdout.strip().decode()
    commit_date = subprocess.run(["git", "log", "-1", "--format=%cd"], stdout=subprocess.PIPE).stdout.strip().decode()
    author = subprocess.run(["git", "log", "-1", "--format=%an"], stdout=subprocess.PIPE).stdout.strip().decode()

    # compares the commit date with the current time
    commit_time = datetime.strptime(commit_date, "%c %z")
    now = datetime.now(timezone.utc)
    days_ago = (now - commit_time).days
    recent_commit = days_ago <= 7
   
    # checks if the author of the most recent commit is Rufus
    commit_by_rufus = author == "Rufus"
    
    # if the active branch needs to be a boolean value the code is below
    # active_branch = bool(branch)
    print("Active branch: ", branch)
    print("Local Changes: ", bool(modified))
    print("Recent Commits: ", recent_commit)
    print("Blame Rufus: ", commit_by_rufus)

# parse the user inputs with a decription for what is needed
if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument("git_dir", help="directory in which to assess git status \n Example Run: python /path/to/wasitRufus.py Path/to/git-directory")
    args = parser.parse_args()
    git_status(args.git_dir)