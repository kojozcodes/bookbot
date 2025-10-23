import sys
from stats import get_word_count, get_character_count, dict_to_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_filepath = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents


def main():
    book_content = get_book_text(book_filepath)
    word_count = get_word_count(book_content)
    character_count = get_character_count(book_content)
    sorted_charaters = dict_to_list(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_charaters:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")


main()
