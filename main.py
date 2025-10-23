from stats import num_words
from stats import num_char
from stats import sorted_num_char

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents



def main():
   file_path = "books/frankenstein.txt"
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {file_path}...")
   print("----------- Word Count -----------")
   print(f"Found {num_words(get_book_text(file_path))} total words")
   print("--------- Character Count -------")
   sorted_list=sorted_num_char(num_char(get_book_text(file_path)))
   for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    
   print("============= END ===============")

main()