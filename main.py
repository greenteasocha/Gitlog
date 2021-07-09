from Reader.reader import Reader


def main():
    hash_value = "bcbcd2445a05e28cfa617f50f5ac4772c9652290"
    r = Reader()
    r.walk_history(hash_value)


if __name__ == "__main__":
    main()
