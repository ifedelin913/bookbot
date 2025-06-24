from stats import word_count
from stats import char_count
from stats import sort_char_count

def get_book_text(file):
    #open local file and read into contents variable
    with open(file) as f: 
        contents = f.read()
    return contents

def main():
    # set text to book variable
    book = get_book_text("books/frankenstein.txt")

    # set text statistics to respective varibales
    count = word_count(book)
    char_counts = char_count(book)
    sorted_list = sort_char_count(char_counts)

    #print text statistics
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for dict in sorted_list:
        print(f"{dict['char']}: {dict['num']}")
    
    print("============= END ===============")

main()
