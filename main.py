from stats import word_count
from stats import count_ch
from stats import sort_items
import sys

def get_book_text(filepath):
    with open(filepath) as fp:
        file_contents = fp.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        sys.exit(1)
        print("Usage: python3 main.py <path_to_book>")

    contents = get_book_text(sys.argv[1])
    print(contents)

    num_words = word_count(contents)
    num_chs = count_ch(contents)

    print(f"""============ BOOKBOT ============"
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    sorted_items = sort_items(num_chs)

    for item in sorted_items:
        ch = item["char"]
        num = item["num"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {num}")
    
    print("============= END ===============")


main()
