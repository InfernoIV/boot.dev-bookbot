#function to count words of a text string
def count_words(text_string):
    #split the file contents
    words = text_string.split()
    #return the length of the array
    return len(words)
