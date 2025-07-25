def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_counts(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetical characters
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda d: d["num"], reverse=True)
    return sorted_list