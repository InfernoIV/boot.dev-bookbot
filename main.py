#main function
def main() :
    #define the path of the book
    path = "./books/frankenstein.txt"
    #get the content of the book
    book_text = get_book_text(path)
    #print the text to console
    print(book_text)

#function to get the content of a file
def get_book_text(path_to_file) :
    #open the file
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

main()