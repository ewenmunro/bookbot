def main():
    with open("books/frankenstein.txt") as f:
        frankenstein = f.read()
        words = frankenstein.split()
        word_count = len(words)
        letter_count = {}

        for word in words:
            for char in word:
                if char.isalpha():
                    char = char.lower()
                    if char in letter_count:
                        letter_count[char] += 1
                    else:
                        letter_count[char] = 1

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print("")

        sorted_letter_count = sorted(
            letter_count.items(), key=lambda item: item[1], reverse=True)

        for letter, count in sorted_letter_count:
            print(f"The '{letter}' character was found {count} times")

        print("")
        print("--- End report ---")


if __name__ == "__main__":
    main()
