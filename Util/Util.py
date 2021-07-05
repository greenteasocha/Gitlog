import os

# find root directory (absolute path) of target git repository
def find_git_root(filepath: str)-> str:
    original = filepath
    roop_count = 0
    MAX_LOOP = 100
    while(True):
        if os.path.exists(os.path.join(filepath, ".git")):
            return filepath

        if filepath == "/":
            raise Exception("Not a git repository: " + original)

        filepath = os.path.abspath(os.path.join(filepath, "../"))

        roop_count += 1
        if roop_count > MAX_LOOP:
            raise Exception("Too much loop in git root finding")
