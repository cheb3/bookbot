from stats import count_words

def main():
    book_path = "books/frankenstein.txt"
    return print(count_words(get_book_text(book_path)))
  

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        book_contents = f.read()
        return book_contents

  
main()