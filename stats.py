def num_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter +=1
    return counter

def num_char(text):
    lowered_text = text.lower()
    chars = list(lowered_text)
    output = {}
    for char in chars:
        if char not in output:
            output.update({char:1})
        else:
            output[char]+=1
    return output
def sort_on(items):
     return items["num"]

def sorted_num_char(dict_chars):
    sorted_char = []
    for dict_char in dict_chars:
            sorted_char.append({"char": dict_char,"num": dict_chars[dict_char]})
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char