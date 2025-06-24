from stats import word_count

def get_book_text(file):
    #open local file and read into contents variable
    with open(file) as f: 
        contents = f.read()
    return contents

def main():
    book = get_book_text("books/frankenstein.txt")
    count_message = word_count(book)
    print(count_message)

main()
