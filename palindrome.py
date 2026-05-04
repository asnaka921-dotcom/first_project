def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print("\n=== PALINDROME CHECKER ===")
text = input("Enter a word or sentence: ")
if is_palindrome(text):
    print(f'"{text}" is a Palindrome ✓')
else:
    print(f'"{text}" is NOT a Palindrome ✗')
