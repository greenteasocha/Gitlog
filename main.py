import sys
from Reader.reader import Reader


def main(hash_value):
    r = Reader()
    r.walk_history(hash_value)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Please input commit hash as args.")
        sys.exit(0)

    main(args[1])
