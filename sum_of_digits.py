import math
num = int(input("Enter the number: "))

def dig_sum(num1):
    if num1 <10:
        return num1
    else: 
        for a in range(10):
            for b in range(10):
                if 10*a + b == num1:
                    ten = a
                    unit = b
        return ten+unit

if num < 100:
    print("the sum of digits is:",dig_sum(num))
else:
    list_of_digits = []
    curr = num
    p = math.floor((math.log(curr,10)))

    while p >= 2:
        for x in range(10):
            for y in range(10):
                if p*x + y == curr:
                    list_of_digits.append(y)
                    curr = x
                    print("reached", curr)
        
    sum_of_digits = dig_sum(curr) + sum(list_of_digits)
    print("The sum of digits is:", sum_of_digits)
