def word_count(text):
    # gather a word count from text and return word count message
    words = text.split()
    count = len(words)

    return f"{count} words found in the document"