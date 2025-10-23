from stats import get_word_count, get_character_count


def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents


def main():
    book_content = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_content)
    character_count = get_character_count(book_content)
    print(book_content)
    print(f"Found {word_count} total words")
    print(character_count)

main()
