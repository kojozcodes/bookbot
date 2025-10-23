def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents


def get_word_count(book_content):
    split_words = book_content.split()
    return len(split_words)


def main():
    book_content = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_content)
    print(book_content)
    print(f"Found {word_count} total words")

main()
