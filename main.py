import sys
from stats import get_word_count, print_char_count

def get_book_text(path):
    try:
        with open(path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error opening file: {path}")
        sys.exit(1)
    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    
    content = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")

    word_count = get_word_count(content)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    print_char_count(content)

    print("============= END ===============")


if __name__ == "__main__":
    main()
