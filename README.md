# WasItRufus

This script prints specific facts about a local git repository.

## Requirements
- Python 3.x

## Usage
python /path/to/wasItRufus.py /path/to/git_repo


## Output
- Current Active branch (String)
- Whether repository files have been modified (boolean)
- Whether the current head commit was authored in the last week (boolean)
- Whether the current head commit was authored by Rufus (boolean)

## Note
- Make sure you have python installed in your system.
- If the provided git_dir is not valid, the script will raise an exception with an appropriate error message.
