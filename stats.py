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


def sort_on(items):
    return items["num"]


def dict_to_list(dictionary):
    character_count_list = []
    for key in dictionary:
        character_count_list.append(
            {"char": key, "num": dictionary[key]}
        )
    character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list
