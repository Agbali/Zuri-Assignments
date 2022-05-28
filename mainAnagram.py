# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    #remove every space and change letters to lowercase
    first_word = word.replace(' ', '').lower()
    the_anagram = anagram.replace(' ', '').lower()

    #ensure that the words are of the same length
    if len(first_word) != len(the_anagram): return False
    
    #forloops to check for each character of each word
    for char in first_word:
        
        if char not in the_anagram:
            return False
   
    return True

print(find_anagram("Hello", "check"))
print(find_anagram("Below", "elbow"))
   
