def count_words(file_contents):
    """Counts words from a text document"""
    num_words = len(file_contents.split())
    return num_words

def char_counts(file_contents):
    """Counts numbers of characters from text document"""
    count = {}
    for char in file_contents:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_key(item):
    return item["num"]

def sort_characters(char_counts):
    report = []
    for char, num in char_counts.items():
        if not char.isalpha():
            continue
    
        report.append({
            "char": char,
            "num": num
        })

    report.sort(key=sort_key, reverse=True)
    return report
