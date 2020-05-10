def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b

print(lesser_of_two_evens(2, 26))



def alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False

print(alliteration("Horrible", "Tiger"))



def laughter(pattern, phrase):
    y = 0
    repetition = 0
    x = len(pattern)
    for letter in phrase:
        if y == x - 1:
            repetition += 1
        y = 0
        index = phrase.index(letter)
        for i in range(1, x):
            if phrase[index + y] == pattern[y]:
                y += 1
            else:
                break
    return repetition


print(laughter("ixi", "ixixixixixixi"))



def lengthen(string, size):
    newstring = ""
    for letter in string:
        newstring += letter * size
    return newstring

print(lengthen('Hello there!', 5))



def twenty_one(num1, num2, num3):
    total = num1 + num2 + num3
    if total > 21 and 11 in (num1, num2, num3):
        total -= 10
    if total > 21:
        return "Bust - {}".format(total)
    else:
        return total

print(twenty_one(4, 8, 9))



def summer_of_69(array1):
    x = True
    total = 0
    for num in array1:
        if num == 6:
            x = False
        if x:
            total += num
        if num == 9:
            x = True
    return total

        
print(summer_of_69([2, 1, 6, 9, 11]))



def bondetector(numlist, numstring):
    runningcount = []
    for num in numlist:
        if num in numstring:
            runningcount.append(num)
    return set(numstring) == set(runningcount)


print(bondetector([4,2,3,8,7,5,6,0,1], [4,3,8,7,5,6,0,1]))



def primes(num):
    prime = True
    primenums = [2]
    for i in range(3, num+1, 2):
        prime = True
        for number in primenums:
            if i % number == 0:
                prime = False
        if prime == True:
            primenums.append(i)
    return primenums

print(primes(101))



def big_letters(letter):
    letters = {"A1":"  *  ", "A2":" * * ", "A3":"*****",
               "A4":"*   *", "A5":"*   *"}
    for i in range(1,6):
       print(letters[ letter.upper() + str(i)])

big_letters("a")


















