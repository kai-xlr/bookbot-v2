import sys 

from stats import (
     num_words,
     char_count, 
    sorted_list,
)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    content = get_book_text(book_path)
    count = num_words(content)
    char_ct = char_count(content)
    sorted = sorted_list(char_ct)

    print_report(book_path, count, sorted)
    
main()
