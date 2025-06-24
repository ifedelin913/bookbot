from stats import word_count
from stats import char_count

def get_book_text(file):
    #open local file and read into contents variable
    with open(file) as f: 
        contents = f.read()
    return contents

def main():
    # set text to book variable
    book = get_book_text("books/frankenstein.txt")

    # set text statistics to respective varibales
    count_message = word_count(book)
    char_counts = char_count(book)

    #print text statistics
    print(count_message)
    print(char_counts)

main()
