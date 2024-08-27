def main():
    book = "/home/urbnauq/documents/Boot_dev/book_bot_remastered/books/frankenstein.txt"
    text = read_book(book)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letters_plus_count = letters_found(letter_count)
    book_report(word_count, letters_plus_count)
    
#Funtions---------------------------------------------------------------------------------------------------------------------   
def read_book(book):
    with open(book) as f:
        file_contents = f.read()
    
    return file_contents
        
def count_words(book):
    words = book.split()
    
    count = 0
    for word in words:
        count += 1
    
    return count

def count_letters(book):
    
    lowered_string = book.lower()
    lowered_string_split = lowered_string.split()
    
    letter_count = {}
    
    for word in lowered_string_split:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
                
    return letter_count

def letters_found(letters):
    
    lst = []
    
    for count in letters:
        if count.isalpha():
            lst.append({"letter": count, "count": letters[count]})
            
    return lst

def sort_on(dict):
    return dict["count"]

def book_report(word_count, letters_plus_count):
    letters_plus_count.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for word in letters_plus_count:
        print(f"The {word["letter"]} character was found {word["count"]} times")
    print("--- End report ---")

main()
