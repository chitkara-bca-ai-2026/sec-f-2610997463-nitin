sentence = "".join(input("Enter a sentence: ").split())
print("=" * 50)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 50)
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")
print()
print("--- Character Breakdown ---")
words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0
for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
print(f"Words:              {words}")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special characters: {special}")
print()
print("--- Summary ---")
total_letters = vowels + consonants
if total_letters > 0:
    percent = (vowels / total_letters) * 100
else:
    percent = 0
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {percent:.1f}%")
print()
print("=" * 50)
print("Analysis Complete!")
print("=" * 50)