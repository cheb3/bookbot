def count_words(book_contents):
    #num_words = 0
    num_words = len(book_contents.split())
    return num_words

def sort_on(sorted_list):
     return sorted_list["num"]
    
def count_chars(book_text):
    character_dict = {}
    for char in book_text:
            char = char.lower()
            if char in character_dict:
                character_dict[char] += 1
            else:
                 character_dict[char] = 1
    return character_dict    

def dict_sort(character_dict):
    sorted_list = []

    for char in character_dict:
        char_num_dict = {}
        char_num_dict["char"] = char
        char_num_dict["num"] = character_dict[char]
        sorted_list.append(char_num_dict)
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

