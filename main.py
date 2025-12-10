import sys
from stats import count_words, count_characters, sorted_char_dict

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_text = get_book_text(sys.argv[1])

    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_counts = sorted_char_dict(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for character_count in sorted_counts:
        char = character_count["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {character_count['num']}")

    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


if __name__ == "__main__":
    main()