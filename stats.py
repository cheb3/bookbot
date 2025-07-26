def count_words(book_contents):
    num_words = 0
    num_words = len(book_contents.split())
    return (f"{num_words} words found in the document")

#print(count_words(get_book_text("books/frankenstein.txt")))