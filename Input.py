#introduction
name=input("Enter you name: ")
age=input("Enter your age: ")
print("hello, my name is "+name +" and I am "+age+ " years old")

#hobby
hobby = input("Enter your favorite hobby: ")
print("Uppercase:", hobby.upper())
print("Lowercase:", hobby.lower())
print("Length of the hobby string:", len(hobby))

#function
def greet_user(name):
    print(f"Welcome {name}, Python is waiting for you!")

user_name = input("Enter your name: ")
greet_user(user_name)

#string function
sentence = input("Enter a sentence: ")
print("Title Case:", sentence.title())
print("Spaces replaced by '-':", sentence.replace(" ", "-"))
print("Without leading/trailing spaces:", sentence.strip())

#Input combination
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
print("Here’s your sentence:")
print("The " + adj + " " + noun + " loves to " + verb + ".")

#return function
def full_name(first, last):
    return first + " " + last

first = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Your full name is:", full_name(first, last))