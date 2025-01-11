def main():
    book_file_path = "books/frankenstein.txt"
    word_count = count_words(get_book_contents(book_file_path))
    character_count = count_characters(get_book_contents(book_file_path))
    print(f"--- Begin report of {book_file_path} ---")
    print(f"{word_count} words found in the document\n")
    for key, val in character_count.items():
        print(f"The '{key}' character was found {val} times")
    print("--- End report ---")

def get_book_contents(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        return file_contents

def count_words(book_contents):
    word_count = len(book_contents.split())
    return word_count

def count_characters(book_contents):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chars_dict = {}
    for c in book_contents.lower():
        if c in alphabet and c not in chars_dict:
            chars_dict[c] = 1
        elif c in alphabet and c in chars_dict:
            chars_dict[c] += 1
    return chars_dict

if __name__ == "__main__":
    main()