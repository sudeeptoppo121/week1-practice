def count_words(sentence):
    words = sentence.lower().split()
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict


# Input Section
user_sentence = input("Enter a sentence: ")

# Call Function
word_freq = count_words(user_sentence)

if word_freq:
    total_words = sum(word_freq.values())
    unique_words = len(word_freq)

    # max() returns the first word encountered in case of a tie in frequency
    most_frequent_word = max(word_freq, key=word_freq.get)

    # Display Section
    print("\n--- Word Frequency Analysis ---")
    print(f"Word Frequencies: {word_freq}")
    print(f"Total Number of Words: {total_words}")
    print(f"Number of Unique Words: {unique_words}")
    print(
        f"Most Frequent Word: '{most_frequent_word}' (Count:"
        f" {word_freq[most_frequent_word]})"
    )
else:
    print("No words were entered.")