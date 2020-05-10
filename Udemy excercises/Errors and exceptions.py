def add(n1, n2):
    return n1 + n2

n1 = 1
n2 = "2"

try:#Attempt code
    print(add(n1, n2))
except:#Run if 'try' has error
    print("Oops, didn't add two numbers!")
else:#Run if 'try' has no errors
    print("Good stuff!")
finally:#Always run
    print("Addition is Fun!")
