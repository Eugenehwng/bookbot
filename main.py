from stats import get_word_count, get_char_count, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    
    return contents

def print_report(filepath, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}...')
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for item in char_count:
        print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    
    word_count = get_word_count(contents)
    
    char_count = get_char_count(contents)
    sorted_char_count = sort_dictionary(char_count)
    
    print_report(filepath, word_count, sorted_char_count)
    


main()