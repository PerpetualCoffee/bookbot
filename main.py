import sys
from stats import count_words, char_counts, sort_characters

def get_book_text(path_to_file): 
    """reads a text file and returns as a string"""
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    # check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    text = get_book_text(filename)
    num_words = count_words(text)
    count_chars = char_counts(text)
    sorted_report = sort_characters(count_chars)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_report:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

