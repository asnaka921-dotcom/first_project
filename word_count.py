def count_words(sentence):
    if not sentence.strip():
        return 0
    return len(sentence.split())

print("\n=== WORD COUNTER ===")
sentence = input("Enter a sentence: ")
total = count_words(sentence)
print(f"Total words: {total}")
