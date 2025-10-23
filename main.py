def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents


def main():
    print(get_book_text("books/frankenstein.txt"))


main()
