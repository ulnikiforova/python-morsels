import re
def count_words(str):
    # words = re.split(r'\W+', str) # only Unicode alphanumeric words + underscore
    words = str.split() # words separated by whitespaces only
    words_count = dict.fromkeys(words,0)
    for item in words:
        words_count[item] += 1
    return words_count

print(count_words("don't stop believing"))