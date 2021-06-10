# ----------------------------SUAL----------------------------------------------------------------------------

# 1)
array = [8, 2, 3, 0, 7]
def a(x):
    Sum = 0
    for i in x:
        Sum += i
    print(Sum)
a(array)



# 2)
def multiply (numbers):
    total = 1
    for x in numbers:
        total *= x
    return(total)

print(multiply((8, 2, 3, -1, 7)))



# 3)
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