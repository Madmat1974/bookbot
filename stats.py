
#FUNCTION TO COUNT THE NUMBER OF WORDS IN A STRING
def get_number_of_words(text):
    words = []
    words = text.split()
    return len(words)

#FUNCTION TO READ A FILE AND RETURN THE CONTENTS IN A STRING
def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text

#FUNCTION TO COUNT THE NUMBER OF EACH CHARACTER FROM A STRING RETURNING A DICTIONARY
def number_of_each_character(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

#FUNCTION TO SORT A DICTIONARY BY VALUE AND RETURN A DICTIONARY IN DESCENDING ORDER
def sort_dict_by_value(d):
    sorted_list = sorted(d.items(), key = lambda x:x[1], reverse = True)
    convert_dict = dict(sorted_list)
    return convert_dict

#FUNCTION TO PRINT OUT STATS OF THE BOOK
def print_report(word_count, character_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in character_count:
        print(f"{letter}: {character_count[letter]}")
    print("============= END ===============")