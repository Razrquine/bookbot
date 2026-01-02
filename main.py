def count_words(book_contents):
    list_of_words = book_contents.split()
    return len(list_of_words)


def get_book_text(file_path):
    book_contents = ""
    with open(file_path) as f:
        book_contents = f.read()
    return book_contents


def main():
    frankenstein_contents = get_book_text("./books/frankenstein.txt")
    print(frankenstein_contents)
    print(f"Found {count_words(frankenstein_contents)} total words")


main()
