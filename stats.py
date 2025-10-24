def num_words(book):
    return len(book.split())

def char_count(varia):
    chars = {}
    for c in varia:
        lower = c.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars

def sort_on(d):
    return d["num"]

def sorted_list(chara):
    sorted_list = []
    for ch in chara:
        sorted_list.append({"char": ch, "num": chara[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
