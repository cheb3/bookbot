def get_book_text(book_file_path):
    with open(book_file_path) as f:
        book_contents = f.read()
        return book_contents

def count_words(book_text):
    num_words = 0
    num_words = len(book_text.split())
    return (f"{num_words} words found in the document")

def main():
    return print(count_words(get_book_text("books/frankenstein.txt")))
    
main()