def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    count = count_letters(text)
    count_words = count_woords(text)
    list_of_dict = dict_in_list_dict(count)
    list_of_dict.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")
    print()

    for item in list_of_dict:
        print(f"The '{item['symbol']}' character was found {item['count']} times")

    print("--- End report ---")



def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_woords(text):
    words = text.split()
    return len(words)

def count_letters(text):
    count = {}
    for i in text:
        if i.isalpha():
            low = i.lower()
            if low in count:
                count[low] += 1
            else:    
                count[low] = 1
    return count

def dict_in_list_dict(dict):
    list_of_dict = [{"symbol": key, "count": value} for key, value in dict.items()]
    return list_of_dict

def sort_on(dict):
    return dict["count"]
    

main()