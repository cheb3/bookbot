from stats import count_words
from stats import count_chars
from stats import dict_sort
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    character_count = count_chars(book_text)
    sorted_list = dict_sort(character_count)
    #dict_sort(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        #print(dict)
        char = dict["char"]
        num = dict["num"]
        if char.isalpha() == True:
            print(f"{char}: {num}")
    print("============= END ===============")

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        book_contents = f.read()
        return book_contents





  
main()