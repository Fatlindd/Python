
with open('Files/check_words.txt', 'rt') as file:
    words = file.read().split()

def countWordsEndsWithE(words):
    count = 0 
    for word in words:
        # 🔔 using negative index 
        if word[-1] == 'e':
            count += 1
    return count

print(f"words that ends with 'e' are: {countWordsEndsWithE(words)}")