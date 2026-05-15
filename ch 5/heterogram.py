def heterogram(word):
    word = word.lower()

    if len(word) == len(set(word)):    #set(word) will remove duplicates and return unique characters
        print("Heterogram")
    else:
        print("Not a Heterogram")

text = input("Enter a word: ")
heterogram(text)