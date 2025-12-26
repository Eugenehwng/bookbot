def get_word_count(text):
    return len(text.split())


def get_char_count(text):
    counts = {}
    for c in text:
        if c.isalpha():
            counts[c.lower()] = counts.get(c.lower(), 0) + 1
    
    return counts

def sort_on(items):
    return items["num"]

def sort_dictionary(dict):
    sorted_dict = []
    for c in dict:
        sorted_dict.append({"char": c, "num": dict[c]})
    
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict
        