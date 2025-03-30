def word_count(book_text: str):
    list_of_words = book_text.split()
    word_count = len(list_of_words)                                
    return word_count

def character_count(book_text:str):
    lower_case_text = book_text.lower()
    character_list = list(lower_case_text)
    character_count_dict = {}
    for character in character_list:
        if character in character_count_dict:
            character_count_dict[character] += 1
        else:
            character_count_dict[character] = 1
    return character_count_dict


def sort_on(dict):
    return dict["count"]


def sort_dict(dict):
    sorted_list = []
    for k,v in dict.items():
        kv_pair = {"character" : k, "count" : v}
        sorted_list.append(kv_pair)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        

