def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_content = get_book_text(frankenstein_path)
    frankenstein_word_count = get_word_count(frankenstein_content)
    frankenstein_letter_count = get_letter_count(frankenstein_content)

    print(f"Simple stats of {frankenstein_path}")
    print(f"Word count: {frankenstein_word_count}")
    print(f"Letter occurence count:")
    print_dictionary(frankenstein_letter_count)
    print(f"Sorted letter occurence count:")
    print_dictionary(sort_dictionary_by_value(frankenstein_letter_count))


def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()

    return book_contents


def get_word_count(book_contents):
    return len(book_contents.split())


def get_letter_count(book_contents):
    lowercased_book_contents = book_contents.lower()
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    letter_to_count_dict = {}

    for alpha_letter in alphabet:
        letter_to_count_dict[alpha_letter] = 0

        for book_letter in lowercased_book_contents:
            if book_letter == alpha_letter:
                letter_to_count_dict[alpha_letter] += 1

    return letter_to_count_dict


def sort_dictionary_by_value(dictionary):
    # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
    # This somehow sorts a dictionary by values in just one line but I don't really understand it
    # return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    listed_dictionary = []
    sorted_dictionary = {}

    for item in dictionary:
        listed_dictionary.append({"char": item, "num": dictionary[item]})

    listed_dictionary.sort(key=sort_on, reverse=True)

    for item in listed_dictionary:
        sorted_dictionary[item["char"]] = item["num"]

    return sorted_dictionary


def sort_on(d):
    return d["num"]


def print_dictionary(dict):
    for key in dict.keys():
        print(f"{key}: {dict[key]}")


main()
