# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):

    # [assignment] Add your code here 
    with open('story.txt', 'r') as file:
        filename = file.read()
    return filename 

print(read_file_content('story.txt')) 

def count_words():
    text = read_file_content("./story.txt")
    
    # [assignment] Add your code here

    counted_text = text.split(" ")

    number_of_words = {}

    for i in counted_text:
        if i in number_of_words:
            number_of_words[i] += 1

        else:
            number_of_words[i] = 1
            
    return number_of_words
print(count_words())
    # return {"as": 10, "would": 20}
