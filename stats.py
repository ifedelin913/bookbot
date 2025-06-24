def word_count(text):
    # gather a word count from text and return word count message
    words = text.split()
    count = len(words)

    return count

def char_count(text):
    # create empty dictionary for character counts
    char_count = {}

    # iterate over each character in the text, if the character is in dict,
    # increment by one, else add new key pair with the character
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_on(items):
    return items["num"]

def sort_char_count(chars):
    char_list = [] # initialize empty list to store dicts

    # iterate over each item of the dictionary, stored as char and count
    # if char is alphabetical then it is stored as a dictionary with two
    # key pairs in the char_list dict
    for char, count in chars.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    # char_list is sorted in reverse order by the "num" key pair value
    char_list.sort(reverse = True, key = sort_on)

    return char_list