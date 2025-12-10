def count_words(book_text):
    words = book_text.split()
    return len(words)


def count_characters(book_text):
    counts = {}
    for char in book_text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_on(item):
    return item["num"]


def sorted_char_dict(char_count_dict):
    sorted_list = []

    for char, count in char_count_dict.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list