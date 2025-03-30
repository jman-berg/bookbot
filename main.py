from stats import character_count, sort_dict, word_count 
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main (path_to_file):
    book_text = get_book_text(path_to_file)
    num_words = word_count(book_text)
    count = character_count(book_text)
    sorted = sort_dict(count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")

main(sys.argv[1])


    
