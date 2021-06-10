# ----------------------------SUAL----------------------------------------------------------------------------

# 1)Write a Python function to sum all the numbers in a list.


array = [8, 2, 3, 0, 7]
def a(x):
    Sum = 0
    for i in x:
        Sum += i
    print(Sum)
a(array)



# 2)Write a Python function to multiply all the numbers in a list. 

array = [8, 2, 3, -1, 7]
def a(x):
    total = 1
    for i in x:
        total *= i
    print(total)

print(a(array))



# 3)Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.).
#  If the number is less than 1 or greater than 7, the function should return None.
returnDay = {
1: 'Monday',
2: 'Tuesday',
3: 'Wednesday',
4: 'Thursday',
5: 'Friday',
6: 'Saturday',
7: 'Sunday',

}
 
def day(number):
    try:
        return returnDay[number]
    except:
        return "error"

print(day(5))


# 4)
def LastElement(list):
    for i in list:
        if i == list[-1]:      
            return i
        else:
            if i == []:
                return "none"
    
print(LastElement((1,2,3,4,5,7)))


# 5)
def even(list):
    a = []
    for i in list:
        if i % 2 == 0:
            a.append(i)
    return a

print(even((1,2,3,4,5,6,7,8,9,10)))