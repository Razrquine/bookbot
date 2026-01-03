from stats import char_count, count_words, sort_dict


def get_book_text(file_path):
    book_contents = ""
    with open(file_path) as f:
        book_contents = f.read()
    return book_contents


def main():
    file_path = "books/frankenstein.txt"
    frankenstein_contents = get_book_text(file_path)
    frankenstein_word_count = count_words(frankenstein_contents)
    frankenstein_sorted_char_count = sort_dict(char_count(frankenstein_contents))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_word_count} total words")
    print("--------- Character Count -------")

    for item in frankenstein_sorted_char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


main()
