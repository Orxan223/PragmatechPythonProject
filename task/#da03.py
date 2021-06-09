# 1)
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return(total)

print(sum((8, 2, 3, 0, 7)))

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

