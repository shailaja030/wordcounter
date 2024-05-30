def count_words_in_sentence():
    sentence = input("Enter the sentence: ").strip()
    
    if not sentence:
        print("No sentence entered. Please enter a valid sentence.")
        return
    
    word_list = sentence.split()
    word_count = len(word_list)
    
    print(f"Original sentence: \"{sentence}\"")
    print(f"Number of words in the above sentence: {word_count}")

# Call the function to execute the word counter program
count_words_in_sentence()