#FUNCTIONS

def function_machine(name = "Default name if no arguments are given."):
    print("Hello", name)

    #return ends the function, call at the end
    return "Herro"

#Runs the function, and then prints whatever is returned
print(function_machine("Conor"))


#PIG LATIN EXCERSISE
def piglatinify(word):
    if word[0].lower() in "aeiou":
        word += "ay"
    else:
        letter1 = word[0]
        word = word[1:] + letter1 + "ay"

    return word.capitalize()

PigLatinWord = piglatinify("Word")
print(PigLatinWord)


#Unlimited arguments
def addition(*args):
    return sum(args)

print(addition(5, 6, 4, 7, 3))

#Unlimited dictionary items
def names(**kwargs):
    if 'boysname' in kwargs:
        return("Hello male! You are there somewhere, I can smell you. "
               "Aah, it is {}".format(kwargs["boysname"]))

print(names(girlsname = "Maeve", boysname = "Conor", womansname = "Maire"))





















