def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text, include_spaces):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))


def count_sentences(text):
    # basic sentence counting: by periods, exclamation marks, and question marks
    sentence_endings = [".", "!", "?"]
    count = 0
    for char in text:
        if char in sentence_endings:
            count += 1
    if count == 0 and text.strip():
        count = 1
    return count


def analyze_text(text):
    word_count = count_words(text)
    char_count_with_spaces = count_characters(text, True)
    char_count_without_spaces = count_characters(text, False)
    sentence_count = count_sentences(text)

    if sentence_count > 0:
        words_per_sentence = word_count / sentence_count
    else:
        words_per_sentence = 0
    if word_count > 0:
        chars_per_word = char_count_with_spaces / word_count
    else:
        chars_per_word = 0

    print("==== Text Analysis Result ====")
    print(f"Word count: {word_count}")
    print(f"Characters (spaces included): {char_count_with_spaces}")
    print(f"Characters(spaces not included): {char_count_without_spaces}")
    print(f"Sentence count: {sentence_count}")
    print(f"Average words per sentence: {words_per_sentence:.1f}")
    print(f"Average characters per word: {chars_per_word:.1f}")

    reading_time_minutes = word_count / 225
    if reading_time_minutes < 1:
        reading_time_seconds = reading_time_minutes * 60
        print(f"Estimated reading time: {reading_time_seconds:.1f} seconds")
    else:
        print(f"Estimated reading time {reading_time_minutes:.1f} minutes")


def main():
    print("==== WORD COUNTER ====")
    print("Count words, characters, and sentences in your text")

    while True:
        user_choice = input("Choose an option:"
                            "\n.1 Enter text to analyze"
                            "\n2. Exit"
                            "\nYour choice (1/2): ")
        if user_choice == "1":
            print("Enter or paste your text below (press Enter twice to finish):")
            lines = []

            # If user enters Enter twice, break the loop. Else, append the line they wrote
            while True:
                line = input()
                if not line and not lines[-1]:
                    break
                lines.append(line)

            text = "\n".join(lines)
            if not text.strip():
                print("No text provided. Please try again.")
                continue
            analyze_text(text)

        elif user_choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


main()
