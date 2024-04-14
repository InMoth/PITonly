import argparse 

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)


def main() -> None:
    parser = argparse.ArgumentParser(description="счетчик уникальных слов в тексте")
    parser.add_argument("--text", type=str, help="получает на вход кусок параграфа")

    args = parser.parse_args()

    if args.text:
        print(f"Количество уникальных слов в тексте: {count_unique_words(args.text)}")


if __name__ == "__main__":
    main()


