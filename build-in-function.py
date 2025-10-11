phrase="  Hey this is a string  "
print(phrase.upper())
print(phrase.lower())
print(phrase.title())        # Capitalize the first letter of every word
print(phrase.capitalize())   # Capitalize only the first letter of the string
print(phrase.swapcase())     # Swap uppercase to lowercase and vice versa
print(phrase.islower())
print(phrase.isupper())
print(phrase.lower().islower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3]) #to get character of specific index
print(phrase.index('t'))#to get index of specific character 
print(phrase.replace("Hey","Hello"))#to replace any word or letter in a string

print(phrase.strip())       # Remove spaces (or given chars) from both ends
print(phrase.lstrip())      # Remove spaces (or given chars) from left side
print(phrase.rstrip())      # Remove spaces (or given chars) from right side

print(phrase.startswith("He"))   # Check if string starts with given substring
print(phrase.endswith("ng"))     # Check if string ends with given substring
print(phrase.isalpha())           # True if all characters are alphabets
print(phrase.isdigit())           # True if all characters are digits
print(phrase.isalnum())        # True if all characters are alphanumeric
print(phrase.isspace())           # True if all characters are spaces
print(phrase.istitle())   # True if each word starts with a capital letter

print(phrase.split(","))                  # Split string into a list by separator
print(phrase.join(["a", "b", "c"]))          # Join list elements into a single string

print(phrase.find("o"))        # Return index of substring (or -1 if not found)
print(phrase.rfind("o"))       # Return last index of substring (search from right)
print(phrase.count("l"))       # Count occurrences of a substring

print(phrase.center(4))       # Center align string within given width
print(phrase.ljust(3))        # Left align string within given width
print(phrase.rjust(5))        # Right align string within given width
print("Hey".zfill(5))           # Pad string with zeros on the left
print(phrase.encode())         # Convert string to bytes format