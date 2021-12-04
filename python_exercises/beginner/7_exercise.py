#Return the count of a given substring from a string

def get_count(sentence, counter):
    x = sentence.count(counter)
    print(x)

sent = input("Enter a sentence with multiple of the same word > ")
wrd_cnt = input("Enter word to count > ")

get_count(sent, wrd_cnt)

