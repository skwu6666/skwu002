import math

def mean(values):
    return sum(values)*1.0/len(values)

def stanDev(values):
    length = len(values)
    m = mean(values)
    total_1 = 0
    for i in range(length):
        total_1 += (values[i]-m)**2
    square_root = total_1*1.0/length
    return math.sqrt(square_root)

y=[1,2,3]
xbar=mean(y)
print(xbar)
std=stanDev(y)
print(std)

