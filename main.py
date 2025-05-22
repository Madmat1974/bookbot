import sys
from stats import get_number_of_words, get_book_text, number_of_each_character, sort_dict_by_value, print_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        sorted_dict = {}
        number_of_words = get_number_of_words(text)
        character_dict = number_of_each_character(text)
        sorted_dict = sort_dict_by_value(character_dict)
        print_report(number_of_words, sorted_dict)
    

main()