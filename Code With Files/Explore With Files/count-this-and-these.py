
with open('Files/check_words.txt', 'rt') as file:
    words = file.read().split()

def count_this_and_these(words):
    count = 0
    for word in words:
        if word == 'this' or word == 'these':
            count += 1
    print(f"Number of words 'this' and 'these' are: {count}")

count_this_and_these(words)