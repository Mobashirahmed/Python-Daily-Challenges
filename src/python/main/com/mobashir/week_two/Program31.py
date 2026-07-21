# Check whether a character is a vowel or the letter 'y'.

# Change this letter to test different characters
char = "e"

# Convert to lowercase to handle capital letters
lower_char = char.lower()

# Check if the character is a vowel OR the letter 'y'
is_vowel_or_y = (
    lower_char == "a"
    or lower_char == "e"
    or lower_char == "i"
    or lower_char == "o"
    or lower_char == "u"
    or lower_char == "y"
)

# Print the final boolean outcome
print(f"Is '{char}' a vowel or 'y'?", is_vowel_or_y)