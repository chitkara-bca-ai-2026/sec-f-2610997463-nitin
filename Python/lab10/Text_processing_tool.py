#  Text Processing Tool

print("========================================")
print(" TEXT PROCESSING TOOL")
print("========================================")

# input from user
sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")
# Character at specific position using indexing
pos = int(input("Enter position for indexing: ")) # Konsi position chahiye
if pos < len(sentence): # Check karna position range me hai ya nahi
    print(f"Character at position {pos} : '{sentence[pos]}'") # Indexing se character nikalna

# String slicing karna
start = int(input("Enter start index for slicing : ")) # Start index
end = int(input("Enter end index for slicing : ")) # End index
sliced = sentence[start:end] # Slicing [start:end] se part nikalna
print(f"Sliced string [{start}:{end}] : '{sliced}'")

#  convert in uppercase using upper() fxn.
upper_text = sentence.upper() 
print(f"Uppercase : {upper_text}")

# Lowercase convert
lower_text = sentence.lower() # using  lower() fxn. to print small letters
print(f"Lowercase : {lower_text}")

# word replacement
word_old = input("Enter word to replace : ") 
word_new = input("Enter replacement word : ") 
replaced_text = sentence.replace(word_old, word_new) 
print(f"After replace : {replaced_text}")

# for length
length = len(replaced_text) if word_old in sentence else len(sentence) # len()fxn. for find length 

print(f"Length of sentence : {len(sentence)}")

print("\n========================================")
print("Analysis Complete!")
print("========================================")