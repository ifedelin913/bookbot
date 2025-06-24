def word_count(text):
    # gather a word count from text and return word count message
    words = text.split()
    count = len(words)

    return f"{count} words found in the document"

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