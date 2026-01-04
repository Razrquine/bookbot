import sys

from stats import char_count, count_words, sort_dict


def get_book_text(file_path):
    book_contents = ""
    with open(file_path) as f:
        book_contents = f.read()
    return book_contents


def main():
    print("Usage: python3 main.py <path_to_book>")

    file_path = sys.argv[1]
    book_contents = get_book_text(file_path)
    book_word_count = count_words(book_contents)
    book_sorted_char_count = sort_dict(char_count(book_contents))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")

    for item in book_sorted_char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


main()
