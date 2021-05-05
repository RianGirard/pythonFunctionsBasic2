# 1 Countdown
# accept a number as input; return a new list that counts down from that number to zero inclusive
def countdown(a):
    lis = []
    for x in range(a,-1,-1):
        lis.append(x)
    return lis
print(countdown(15))

#2 Print and Return
# accept a list with two numbers; print first value and return second
def print_and_return(a):
    print(a[0])
    return(a[1])
print(print_and_return([1,2]))

#3 First Plus Length
# accept a list; return the sum of the first value plus the length of the list
def first_plus_length(a):
    y = a[0] + len(a)
    return y
print(first_plus_length([5,2,3,4,5]))  # answer is 5 + 5

#4 Values Greater than Second
# accept a list; create new list with values from orig that are > its 2nd value; print how many this is and return new list; if list < 2 elements, then return False
def values_greater_than_second(a):
    lis = []
    count = 0
    if len(a) < 2:
        return False
    for x in range(len(a)):
        if a[x] > a[1]:
            print(a[x], a[1])
            lis.append(a[x])
            count = count + 1
    print (count)
    return (lis)
print(values_greater_than_second([5,2,3,2,1,4]))

#5 This Length, That Value
# accept two integer parameters: size and value; return a list in length of size with all the given values
def length_and_value(a,b):
    lis = []
    for x in range(a):
        lis.append(b)
    return lis
print(length_and_value(6,2))