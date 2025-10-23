def get_word_count(book_content):
    split_words = book_content.split()
    return len(split_words)


def get_character_count(book_content):
    char_count = {}
    for char in book_content.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
