#python3 main.py


#imports
from stats import count_words, count_characters, sort_characters
import sys

#main function
def main() :
    #if not correct arguments
    if len(sys.argv) != 2:
        #print help message
        print("Usage: python3 main.py <path_to_book>")
        #stop
        sys.exit(1)
        #needed?
        return
    
    
    #define the path of the book
    path_to_file = sys.argv[1] #"books/frankenstein.txt"
    print_report(path_to_file)


#function to get the content of a file
def get_book_text(path_to_file) :
    #open the file
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents


def print_report(path_to_file):
    #get the content of the book
    book_text = get_book_text(path_to_file)

    #get the amount of words
    words_amount = count_words(book_text)
    #get the amount of characters
    character_list = count_characters(book_text)
    #sort the list
    character_list_sorted = sort_characters(character_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...") 
    
    print("----------- Word Count ----------")
    #print the text to console
    print(f"Found {words_amount} total words")
  
    print("--------- Character Count -------")
    #print the text to console
    
    #for each key
    for character in character_list_sorted:
        #print(f"character: {character}")
        #if not a special character
        if character["name"].isalpha():
            #print to console
            print(f"{character["name"]}: {character["num"]}")
            #f: 8451


main()