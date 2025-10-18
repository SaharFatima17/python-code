#string analyzer

def analyze_text(text):
    # Print the length of the text
    print("Length of text:", len(text))
    
    # Print the text in uppercase
    print("Text in uppercase:", text.upper())
    
    # Print the first and last characters
    if len(text) > 0:
        print("First character:", text[0])
        print("Last character:", text[-1])
    else:
        print("The text is empty.")


# Ask user for input
sentence = input("Enter a sentence: ")
analyze_text(sentence)


#Story Creation

def make_story(name, place, object, feeling):
    story = (
        "One day, " + name + " went to " + place +
        " and found a mysterious " + object + ". "
        + name + " felt very " + feeling + " about it!"
    )
    return story


name = input("Enter a name: ")
place = input("Enter a place: ")
object = input("Enter an object: ")
feeling = input("Enter a feeling: ")


print("\nYour Story:")
print(make_story(name, place, object, feeling))


#Word Formatter

def format_word(word):
    # Word in title case
    print("=> Title Case:", word.title())
    
    # Word reversed using slicing
    print("=> Reversed:", word[::-1])
    
    # Replace all vowels with '*'
    formatted_word = word.replace('a', '*')
    formatted_word = formatted_word.replace('e', '*')
    formatted_word = formatted_word.replace('i', '*')
    formatted_word = formatted_word.replace('o', '*')
    formatted_word = formatted_word.replace('u', '*')
    formatted_word = formatted_word.replace('A', '*')
    formatted_word = formatted_word.replace('E', '*')
    formatted_word = formatted_word.replace('I', '*')
    formatted_word = formatted_word.replace('O', '*')
    formatted_word = formatted_word.replace('U', '*')
    
    print("=> Vowels Replaced:", formatted_word)


word = input("Enter a word: ")
format_word(word)
