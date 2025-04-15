#imports
from stats import count_words, count_characters

#main function
def main() :
    #define the path of the book
    path = "./books/frankenstein.txt"
    #get the content of the book
    book_text = get_book_text(path)

    #get the amount of words
    words_amount = count_words(book_text)
    #print the text to console
    print(f"{words_amount} words found in the document")

    #get the amount of characters
    character_amount = count_characters(book_text)
    #print the text to console
    print(f"{character_amount}")

#function to get the content of a file
def get_book_text(path_to_file) :
    #open the file
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents



main()