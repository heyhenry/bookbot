def main():
    book_file_path = "books/frankenstein.txt"
    word_count = count_words(get_book_contents(book_file_path))
    print(f"{word_count} words found in the book: Frankenstein!")

def get_book_contents(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        return file_contents

def count_words(book_contents):
    word_count = len(book_contents.split())
    return word_count

if __name__ == "__main__":
    main()