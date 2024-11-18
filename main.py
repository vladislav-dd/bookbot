def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_word = word_couter(text)
    char_count = character_counter(text)

    print_report(count_word, char_count)

def print_report(words, char):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("\n")
    for cha in char:
        print(f"The '{cha[0]}' character was found {cha[1]} times")
    print("--- End report ---")

def character_counter(text):
    res = {}
    lower_text = text.lower()

    for char in lower_text:
        if char.isalpha():
            if char in res:
                res[char] += 1
            else:
                res[char] = 1

    sorted_res = sorted(res.items(), key=lambda item: item[1],reverse=True)

    return sorted_res


def word_couter(text):
    count = 0
    words = text.split()
    count = len(words)
    return count

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()