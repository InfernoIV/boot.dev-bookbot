#function to count words of a text string
def count_words(text_string):
    #split the file contents
    words = text_string.split()
    #return the length of the array
    return len(words)



def count_characters(text_string):
    #convert to lowercase
    normalized_text = text_string.lower()
    #create a dictionary
    character_set = dict()
    #for each character
    for character in normalized_text:
        #if not in dictionary
        if character not in character_set:
            #create an index and set to 1
            character_set[character] = 1
        else:
            #up the value
            character_set[character] += 1
    #return the dictionary
    return character_set



def sort_characters(character_list):
    #create local copy
    list_characters = []
    
    for character in character_list:
        value = character_list[character]
        list_characters.append({"name": character, "num": value})

    #sort the list
    list_characters.sort(reverse=True, key=sort_on)
    
    #return the list
    return list_characters



# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]
