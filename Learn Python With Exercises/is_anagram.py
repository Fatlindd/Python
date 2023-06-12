
def is_anagram(word1, word2):
    # if word1 = 'code', sorted(word1) => ['c', 'd', 'e', 'o']
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
    
firstWord = input('> First Word: ')
secondWord = input('> Second Word: ')
print(is_anagram(firstWord, secondWord))