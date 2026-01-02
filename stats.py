def count_words(book_contents):
    list_of_words = book_contents.split()
    return len(list_of_words)


def character_count(book_contents):
    character_dict = {}

    for char in book_contents:
        formatted_char = char.lower()
        if formatted_char in character_dict:
            character_dict[formatted_char] += 1
        else:
            character_dict[formatted_char] = 1

    return character_dict
