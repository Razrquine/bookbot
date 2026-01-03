def count_words(book_contents):
    list_of_words = book_contents.split()
    return len(list_of_words)


def char_count(book_contents):
    character_dict = {}

    for char in book_contents:
        formatted_char = char.lower()
        if formatted_char in character_dict:
            character_dict[formatted_char] += 1
        else:
            character_dict[formatted_char] = 1

    return character_dict


def sort_on(items):
    return items["num"]


def sort_dict(dict):
    list_of_dictionaries = []
    for item in dict:
        list_of_dictionaries.append({"char": item, "num": dict[item]})
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries
