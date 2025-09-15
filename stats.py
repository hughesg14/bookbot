def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_ch(text):
    text_unique = text.lower()
    counts = {}
    for ch in text_unique:
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    return counts

def sort_on(items):
    return items["num"]

def sort_items(items):
    items_list = []
    for ch, num in items.items():
        items_list.append({"char":ch, "num": num})
    items_list.sort(reverse=True, key=sort_on)
    return items_list


