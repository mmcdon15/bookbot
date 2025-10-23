from stats import num_words
from stats import num_char
from stats import sorted_num_char
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents



def main():
   #file_path = "books/frankenstein.txt"
   if len(sys.argv)<2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   else:
       file_path = sys.argv[1] 
   text =  get_book_text(file_path)         
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {file_path}...")
   print("----------- Word Count -----------")
   print(f"Found {num_words(text)} total words")
   print("--------- Character Count -------")
   sorted_list=sorted_num_char(num_char(text))
   for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    
   print("============= END ===============")

if __name__ == "__main__":
    main()